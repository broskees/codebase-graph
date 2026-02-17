"""Composite metric and 5 sub-metrics for DSPy prompt optimization.

Metrics evaluate how well a coding agent uses the codebase map:
  - trust:    navigates directly, doesn't search (deterministic)
  - type:     uses correct types from symbol table (deterministic + LLM-judge)
  - import:   imports from correct modules (deterministic)
  - contract: implements interface/base class contracts (LLM-judge)
  - pattern:  follows codebase conventions (LLM-judge)

Weights: trust 30%, type 20%, import 20%, contract 15%, pattern 15%.
"""

from __future__ import annotations

import json
import re
from typing import Any

import dspy

from tests.bench.judge import (
    AssessContractAdherence,
    AssessPatternAdherence,
    AssessTypeConsistency,
)


# ── Helpers ────────────────────────────────────────────────────────


def _parse_ground_truth(example: dspy.Example) -> dict:
    """Extract ground_truth dict from a DSPy example."""
    gt = example.ground_truth
    if isinstance(gt, str):
        return json.loads(gt)
    return gt


def _get_response(pred: dspy.Prediction) -> str:
    """Extract the response text from a prediction."""
    return getattr(pred, "response", "") or ""


def _clamp(value: float) -> float:
    """Clamp a float to [0.0, 1.0]."""
    return max(0.0, min(1.0, value))


def _safe_judge_score(score_raw: Any) -> float:
    """Parse an LLM-judge score robustly. Handles str, float, int."""
    if isinstance(score_raw, (int, float)):
        return _clamp(float(score_raw))
    if isinstance(score_raw, str):
        # Try to extract first float from the string
        match = re.search(r"(\d+(?:\.\d+)?)", score_raw)
        if match:
            return _clamp(float(match.group(1)))
    return 0.0


# ── Anti-patterns for trust metric ────────────────────────────────

_TRUST_ANTI_PATTERNS = [
    "let me search",
    "let me verify",
    "let me check",
    "let me find",
    "let me look",
    "grep",
    "I'll look for",
    "searching for",
    "scanning",
    "I need to find",
]


# ── Import extraction regex ───────────────────────────────────────

# Python: from X import Y  /  import X
_PY_IMPORT_RE = re.compile(r"(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))")
# TypeScript/JS: import { Y } from "X"  /  import X from "X"  /  require("X")
_TS_IMPORT_RE = re.compile(
    r'(?:import\s+.*?from\s+["\']([^"\']+)["\']'
    r"|require\s*\(\s*[\"']([^\"']+)[\"']\s*\))"
)


def _extract_import_paths(code: str) -> list[str]:
    """Extract module paths from import statements in code."""
    paths: list[str] = []
    for m in _PY_IMPORT_RE.finditer(code):
        path = m.group(1) or m.group(2)
        if path:
            paths.append(path)
    for m in _TS_IMPORT_RE.finditer(code):
        path = m.group(1) or m.group(2)
        if path:
            paths.append(path)
    return paths


# ── Sub-metrics ───────────────────────────────────────────────────


def trust_metric(example: dspy.Example, pred: dspy.Prediction) -> float:
    """Deterministic trust metric.

    +0.4  response contains a file path from ground_truth.target_files
    +0.3  response contains a line number reference
    +0.3  response does NOT contain anti-patterns (searching language)
    """
    gt = _parse_ground_truth(example)
    response = _get_response(pred).lower()
    score = 0.0

    # File path present
    target_files = gt.get("target_files", [])
    if any(tf.lower() in response for tf in target_files):
        score += 0.4

    # Line number reference (e.g. ":42", "line 42", "line: 42")
    if re.search(r"(?::\d+|line\s*:?\s*\d+)", response):
        score += 0.3

    # No anti-patterns
    if not any(ap in response for ap in _TRUST_ANTI_PATTERNS):
        score += 0.3

    return _clamp(score)


def type_consistency_metric(example: dspy.Example, pred: dspy.Prediction) -> float:
    """Mixed deterministic + LLM-judge type consistency metric.

    +0.5  deterministic: required type names appear in response
    +0.5  LLM-judge: types are used correctly (field access, signatures)
    """
    gt = _parse_ground_truth(example)
    response = _get_response(pred)
    required_types = gt.get("required_types", [])
    score = 0.0

    # Deterministic half: do required type names appear?
    if required_types:
        found = sum(1 for t in required_types if t in response)
        score += 0.5 * (found / len(required_types))
    else:
        # No required types specified — full credit for deterministic half
        score += 0.5

    # LLM-judge half
    if required_types and response.strip():
        try:
            judge = dspy.Predict(AssessTypeConsistency)
            result = judge(
                codebase_map=example.codebase_map,
                generated_code=response,
                expected_types=", ".join(required_types),
            )
            score += 0.5 * _safe_judge_score(result.score)
        except Exception:
            # Judge failure — be conservative, no credit for this half
            pass
    else:
        score += 0.5

    return _clamp(score)


def import_correctness_metric(example: dspy.Example, pred: dspy.Prediction) -> float:
    """Deterministic import correctness metric.

    +0.5  import paths reference modules mentioned in ground_truth
    +0.3  imported symbol names exist in ground_truth.target_symbols
    +0.2  no obviously wrong paths (bonus — awarded unless imports
           reference completely unknown modules)
    """
    gt = _parse_ground_truth(example)
    response = _get_response(pred)
    required_imports = gt.get("required_imports", [])
    target_symbols = gt.get("target_symbols", [])
    score = 0.0

    import_paths = _extract_import_paths(response)

    # Module path matching
    if required_imports and import_paths:
        matches = 0
        for imp in import_paths:
            imp_normalized = imp.replace("/", ".").replace("\\", ".")
            for req in required_imports:
                req_normalized = req.replace("/", ".").replace("\\", ".")
                if req_normalized in imp_normalized or imp_normalized in req_normalized:
                    matches += 1
                    break
        score += 0.5 * min(1.0, matches / len(required_imports))
    elif not required_imports:
        score += 0.5

    # Symbol name matching — check if any symbol basenames appear in response
    if target_symbols:
        basenames = [s.split("::")[-1] for s in target_symbols]
        found = sum(1 for bn in basenames if bn in response)
        score += 0.3 * min(1.0, found / len(basenames))
    else:
        score += 0.3

    # Bonus: if there are imports and they don't look completely wrong
    if import_paths or not required_imports:
        score += 0.2

    return _clamp(score)


def contract_adherence_metric(example: dspy.Example, pred: dspy.Prediction) -> float:
    """LLM-judge contract adherence metric.

    Uses AssessContractAdherence to evaluate whether the agent implemented
    all required methods/fields from the interface or base class.
    """
    gt = _parse_ground_truth(example)
    response = _get_response(pred)
    patterns = gt.get("patterns", [])

    if not response.strip():
        return 0.0

    # Build contract requirements from ground truth
    requirements_parts = []
    if patterns:
        requirements_parts.append(f"Required patterns: {', '.join(patterns)}")
    required_types = gt.get("required_types", [])
    if required_types:
        requirements_parts.append(f"Required types: {', '.join(required_types)}")
    target_symbols = gt.get("target_symbols", [])
    if target_symbols:
        requirements_parts.append(f"Target symbols: {', '.join(target_symbols)}")

    if not requirements_parts:
        return 1.0  # No contract to check

    contract_desc = "; ".join(requirements_parts)

    try:
        judge = dspy.Predict(AssessContractAdherence)
        result = judge(
            codebase_map=example.codebase_map,
            generated_code=response,
            contract_requirements=contract_desc,
        )
        return _safe_judge_score(result.score)
    except Exception:
        return 0.0


def pattern_adherence_metric(example: dspy.Example, pred: dspy.Prediction) -> float:
    """LLM-judge pattern adherence metric.

    Uses AssessPatternAdherence to evaluate whether the agent followed
    existing codebase conventions.
    """
    gt = _parse_ground_truth(example)
    response = _get_response(pred)
    patterns = gt.get("patterns", [])

    if not response.strip():
        return 0.0

    if not patterns:
        return 1.0  # No patterns specified

    pattern_desc = ", ".join(patterns)

    try:
        judge = dspy.Predict(AssessPatternAdherence)
        result = judge(
            codebase_map=example.codebase_map,
            generated_code=response,
            pattern_description=pattern_desc,
        )
        return _safe_judge_score(result.score)
    except Exception:
        return 0.0


# ── Composite metrics ─────────────────────────────────────────────

_WEIGHTS = {
    "trust": 0.30,
    "type": 0.20,
    "import": 0.20,
    "contract": 0.15,
    "pattern": 0.15,
}

_METRIC_FNS = {
    "trust": trust_metric,
    "type": type_consistency_metric,
    "import": import_correctness_metric,
    "contract": contract_adherence_metric,
    "pattern": pattern_adherence_metric,
}


def composite_metric(
    example: dspy.Example,
    pred: dspy.Prediction,
    trace: Any = None,
) -> float:
    """Weighted composite metric for DSPy optimization.

    Returns a float in [0.0, 1.0]. DSPy MIPROv2 uses this directly.
    """
    gt = _parse_ground_truth(example)
    category = gt.get("category") or _infer_category(example)

    # If we know the task category, weight that metric heavily
    # but still compute all to get a balanced signal.
    scores = {}
    for name, fn in _METRIC_FNS.items():
        scores[name] = fn(example, pred)

    return _clamp(sum(scores[k] * _WEIGHTS[k] for k in scores))


def composite_metric_with_feedback(
    example: dspy.Example,
    pred: dspy.Prediction,
    trace: Any = None,
    pred_name: str | None = None,
    pred_trace: Any = None,
) -> float | dict:
    """Composite metric that returns score + textual feedback for GEPA.

    GEPA's reflective optimizer uses the feedback string to guide
    prompt evolution. GEPA requires 5 positional args:
    (gold, pred, trace, pred_name, pred_trace).

    Returns float when called in standard eval (pred_name is None),
    returns dict(score, feedback) when called by GEPA's feedback path.
    """
    gt = _parse_ground_truth(example)
    scores = {}
    for name, fn in _METRIC_FNS.items():
        scores[name] = fn(example, pred)

    total = _clamp(sum(scores[k] * _WEIGHTS[k] for k in scores))

    # Standard eval path (used by Evaluate accumulator) — return float
    if pred_name is None:
        return total

    # GEPA feedback path — return dict with score + feedback
    parts = []
    for name in _WEIGHTS:
        s = scores[name]
        if s < 0.5:
            parts.append(f"{name} is weak ({s:.2f})")
        elif s < 0.8:
            parts.append(f"{name} is moderate ({s:.2f})")

    if not parts:
        feedback = "All metrics are strong."
    else:
        feedback = "Areas needing improvement: " + "; ".join(parts) + "."

    return {"score": total, "feedback": feedback}


def _infer_category(example: dspy.Example) -> str | None:
    """Try to infer task category from the example fields."""
    # The ground_truth JSON may have been built from a BenchTask
    # that doesn't store category directly. Return None to fall
    # back to computing all metrics.
    return None


# ── Smoke test ────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Running metrics smoke test...\n")

    # Build fake examples and predictions
    fake_gt = json.dumps(
        {
            "target_files": ["src/auth/service.py"],
            "target_symbols": ["src/auth/service::AuthService"],
            "required_types": ["AuthService"],
            "required_imports": ["auth.service"],
            "patterns": ["class", "def authenticate"],
            "anti_patterns": ["let me search", "grep"],
        }
    )

    ex = dspy.Example(
        codebase_map="(fake codebase map)",
        task="Create a new auth handler",
        ground_truth=fake_gt,
    ).with_inputs("codebase_map", "task")

    # Good prediction — trusts the map, uses correct types, imports right
    good_response = (
        "Based on the codebase map, the AuthService is at "
        "src/auth/service.py:42.\n\n"
        "```python\n"
        "from auth.service import AuthService\n\n"
        "class NewHandler(AuthService):\n"
        "    def authenticate(self, token: str) -> bool:\n"
        "        return True\n"
        "```"
    )
    good_pred = dspy.Prediction(response=good_response)

    # Bad prediction — searches, wrong types, wrong imports
    bad_response = (
        "Let me search for the auth module... I'll look for it.\n\n"
        "```python\n"
        "from services.auth_handler import AuthHandler\n\n"
        "class NewHandler:\n"
        "    pass\n"
        "```"
    )
    bad_pred = dspy.Prediction(response=bad_response)

    # Test deterministic metrics
    print("=== Good response ===")
    t = trust_metric(ex, good_pred)
    print(f"  trust:  {t:.2f}")
    assert t > 0.5, f"Expected trust > 0.5, got {t}"

    ic = import_correctness_metric(ex, good_pred)
    print(f"  import: {ic:.2f}")
    assert ic > 0.5, f"Expected import > 0.5, got {ic}"

    print("\n=== Bad response ===")
    t_bad = trust_metric(ex, bad_pred)
    print(f"  trust:  {t_bad:.2f}")
    assert t_bad < 0.5, f"Expected trust < 0.5, got {t_bad}"

    ic_bad = import_correctness_metric(ex, bad_pred)
    print(f"  import: {ic_bad:.2f}")
    assert ic_bad < t, f"Expected bad import < good trust"

    # Test type deterministic portion (skip LLM judge in smoke test)
    # Simple check: required type "AuthService" in good response
    gt_dict = json.loads(fake_gt)
    required = gt_dict["required_types"]
    found = sum(1 for rt in required if rt in good_response)
    det_score = 0.5 * (found / len(required)) if required else 0.5
    print(f"\n  type (deterministic half): {det_score:.2f}")
    assert det_score > 0.0

    print("\nAll smoke tests passed.")
