"""Regression evaluation: compare baseline vs optimized prompt framing.

Reuses the DSPy metric infrastructure to evaluate both prompts on the
full dev set (15 tasks). Prints a comparison table and returns non-zero
if the optimized prompt regresses below the baseline.

Usage:
    OPENROUTER_API_KEY=... python -m tests.bench.run_eval
    OPENROUTER_API_KEY=... python -m tests.bench.run_eval --full   # all 50 tasks
    OPENROUTER_API_KEY=... python -m tests.bench.run_eval --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import dspy
from dspy.evaluate import Evaluate

from tests.bench.metrics import (
    composite_metric,
    contract_adherence_metric,
    import_correctness_metric,
    pattern_adherence_metric,
    trust_metric,
    type_consistency_metric,
)
from tests.bench.tasks import get_all_tasks, get_dev_tasks, to_dspy_examples

# ── Paths ─────────────────────────────────────────────────────────

_BENCH_DIR = Path(__file__).parent
_PROMPTS_DIR = _BENCH_DIR / "prompts"

# ── Prompt loading ────────────────────────────────────────────────


def _load_prompt(name: str) -> str:
    """Load a prompt file from the prompts directory."""
    path = _PROMPTS_DIR / f"{name}.md"
    if not path.exists():
        print(f"Error: prompt file not found: {path}")
        sys.exit(1)
    return path.read_text().strip()


# ── DSPy Signature with custom instruction ────────────────────────


def _make_signature(instruction: str) -> type:
    """Create a DSPy Signature class with a custom docstring/instruction."""

    class CustomAgentResponse(dspy.Signature):
        codebase_map: str = dspy.InputField(
            desc="codebase structural map in TOON format with prompt framing"
        )
        task: str = dspy.InputField(desc="coding task for the agent to perform")
        response: str = dspy.OutputField(desc="agent response with code")

    # DSPy uses the class docstring as the instruction
    CustomAgentResponse.__doc__ = instruction
    return CustomAgentResponse


# ── Evaluation ────────────────────────────────────────────────────


@dataclass
class EvalResult:
    name: str
    composite: float
    trust: float
    type_consistency: float
    import_correctness: float
    contract: float
    pattern: float
    elapsed: float


def evaluate_prompt(
    prompt_name: str,
    instruction: str,
    examples: list,
    lm: dspy.LM,
) -> EvalResult:
    """Evaluate a prompt on the given examples, returning per-metric scores."""
    sig = _make_signature(instruction)
    program = dspy.Predict(sig)
    dspy.configure(lm=lm)

    start = time.time()

    # Run composite metric via Evaluate
    evaluator = Evaluate(
        devset=examples,
        num_threads=4,
        display_progress=True,
        provide_traceback=True,
    )
    result = evaluator(program, metric=composite_metric)
    composite_score = float(result.score)

    # Also compute per-category breakdowns
    # Re-run predictions and score each metric individually
    metric_fns = {
        "trust": trust_metric,
        "type_consistency": type_consistency_metric,
        "import_correctness": import_correctness_metric,
        "contract": contract_adherence_metric,
        "pattern": pattern_adherence_metric,
    }

    per_metric: dict[str, float] = {}
    for metric_name, metric_fn in metric_fns.items():
        scores = []
        for ex in examples:
            try:
                pred = program(codebase_map=ex.codebase_map, task=ex.task)
                scores.append(metric_fn(ex, pred))
            except Exception:
                scores.append(0.0)
        per_metric[metric_name] = sum(scores) / len(scores) if scores else 0.0

    elapsed = time.time() - start

    return EvalResult(
        name=prompt_name,
        composite=composite_score,
        trust=per_metric["trust"],
        type_consistency=per_metric["type_consistency"],
        import_correctness=per_metric["import_correctness"],
        contract=per_metric["contract"],
        pattern=per_metric["pattern"],
        elapsed=elapsed,
    )


def print_results(results: list[EvalResult]) -> None:
    """Print a comparison table of evaluation results."""
    print("\n" + "=" * 80)
    print("REGRESSION EVALUATION RESULTS")
    print("=" * 80)
    print(
        f"{'Prompt':<20} {'Composite':>10} {'Trust':>8} {'Type':>8} "
        f"{'Import':>8} {'Contract':>10} {'Pattern':>9} {'Time':>8}"
    )
    print("-" * 82)

    best_composite = max(r.composite for r in results)
    for r in results:
        marker = " *" if r.composite == best_composite else ""
        print(
            f"{r.name:<20} {r.composite:>9.2f}% {r.trust:>7.2f}% "
            f"{r.type_consistency:>7.2f}% {r.import_correctness:>7.2f}% "
            f"{r.contract:>9.2f}% {r.pattern:>8.2f}% {r.elapsed:>7.1f}s{marker}"
        )

    print("-" * 82)
    winner = max(results, key=lambda r: r.composite)
    print(f"Winner: {winner.name} ({winner.composite:.2f}%)")


def save_regression_results(results: list[EvalResult], output_dir: Path) -> None:
    """Save regression results as JSON for CI tracking."""
    output_dir.mkdir(parents=True, exist_ok=True)
    from datetime import datetime, timezone

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    data = {
        "timestamp": timestamp,
        "results": [
            {
                "name": r.name,
                "composite": r.composite,
                "trust": r.trust,
                "type_consistency": r.type_consistency,
                "import_correctness": r.import_correctness,
                "contract": r.contract,
                "pattern": r.pattern,
                "elapsed": r.elapsed,
            }
            for r in results
        ],
    }
    path = output_dir / f"regression_{timestamp}.json"
    path.write_text(json.dumps(data, indent=2))
    print(f"\nResults saved to {path}")


# ── Main ──────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Regression evaluation: baseline vs optimized prompt"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="evaluate on all 50 tasks (default: dev set of 15)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate setup without running evaluation",
    )
    parser.add_argument(
        "--prompts",
        nargs="+",
        default=["baseline", "optimized_mipro"],
        help="prompt names to evaluate (default: baseline optimized_mipro)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.0,
        help="fail if optimized prompt scores below baseline by this margin",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    # Validate API key
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable required")
        sys.exit(1)

    # Configure LM
    lm = dspy.LM(
        "openrouter/anthropic/claude-sonnet-4.5",
        api_key=api_key,
        max_tokens=2048,
    )

    # Load tasks
    if args.full:
        tasks = get_all_tasks()
        label = "full (50 tasks)"
    else:
        tasks = get_dev_tasks()
        label = "dev (15 tasks)"

    examples = to_dspy_examples(tasks)
    print(f"Evaluation set: {label}")
    print(f"Prompts to evaluate: {', '.join(args.prompts)}")

    # Load prompts
    prompts: dict[str, str] = {}
    for name in args.prompts:
        prompts[name] = _load_prompt(name)
        print(f"  Loaded prompt: {name} ({len(prompts[name])} chars)")

    if args.dry_run:
        print("\n--- DRY RUN ---")
        print(f"API key: {'*' * 8}...{api_key[-4:]}")
        print(f"LM: {lm.model}")
        print(f"Tasks: {len(tasks)}")
        print(f"Prompts: {list(prompts.keys())}")
        for name, text in prompts.items():
            print(f"\n--- {name} (first 200 chars) ---")
            print(text[:200])
        print("\nDry run complete.")
        return

    # Evaluate each prompt
    results: list[EvalResult] = []
    for name, instruction in prompts.items():
        print(f"\n{'=' * 60}")
        print(f"Evaluating: {name}")
        print("=" * 60)
        result = evaluate_prompt(name, instruction, examples, lm)
        results.append(result)

    # Print comparison
    print_results(results)

    # Save results
    save_regression_results(results, _BENCH_DIR / "results")

    # Check regression threshold
    if len(results) >= 2 and args.threshold > 0:
        baseline_score = results[0].composite
        for r in results[1:]:
            if r.composite < baseline_score - args.threshold:
                print(
                    f"\nFAILED: {r.name} ({r.composite:.2f}%) is below "
                    f"baseline ({baseline_score:.2f}%) by more than "
                    f"{args.threshold} points"
                )
                sys.exit(1)

    print("\nRegression check passed.")


if __name__ == "__main__":
    main()
