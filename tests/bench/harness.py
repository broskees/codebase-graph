"""DSPy prompt optimization harness for codebase-graph prompt framing.

Runs MIPROv2 and GEPA optimizers to find the best prompt framing text
that causes coding agents to trust the codebase map, use correct types,
import from the right modules, adhere to API contracts, and follow patterns.

Usage:
    OPENROUTER_API_KEY=... python -m tests.bench.harness
    OPENROUTER_API_KEY=... python -m tests.bench.harness --dry-run
    OPENROUTER_API_KEY=... python -m tests.bench.harness --optimizer mipro
    OPENROUTER_API_KEY=... python -m tests.bench.harness --optimizer gepa
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import dspy
from dspy.evaluate import Evaluate

from tests.bench.metrics import composite_metric, composite_metric_with_feedback
from tests.bench.tasks import get_dev_tasks, get_train_tasks, to_dspy_examples

# ── Paths ─────────────────────────────────────────────────────────

_BENCH_DIR = Path(__file__).parent
_RESULTS_DIR = _BENCH_DIR / "results"
_PROMPTS_DIR = _BENCH_DIR / "prompts"


# ── DSPy Signature (the thing being optimized) ────────────────────


class CodebaseAgentResponse(dspy.Signature):
    """Given a codebase structural map and a coding task, produce a response
    that navigates directly using the map data, maintains type consistency,
    uses correct imports, adheres to API contracts, and follows codebase patterns."""

    codebase_map: str = dspy.InputField(
        desc="codebase structural map in TOON format with prompt framing"
    )
    task: str = dspy.InputField(desc="coding task for the agent to perform")
    response: str = dspy.OutputField(desc="agent response with code")


# ── LM Configuration ─────────────────────────────────────────────


def _get_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        print("Error: OPENROUTER_API_KEY environment variable required")
        print("Get one at https://openrouter.ai/keys")
        sys.exit(1)
    return key


def _configure_lms(api_key: str) -> dict[str, dspy.LM]:
    """Create and return all LM instances."""
    target = dspy.LM(
        "openrouter/anthropic/claude-sonnet-4.5",
        api_key=api_key,
        max_tokens=2048,
    )
    judge = dspy.LM(
        "openrouter/openai/gpt-4.1",
        api_key=api_key,
        max_tokens=1024,
    )
    reflection = dspy.LM(
        "openrouter/anthropic/claude-sonnet-4.5",
        api_key=api_key,
        temperature=1.0,
        max_tokens=2048,
    )
    return {"target": target, "judge": judge, "reflection": reflection}


# ── Optimization ──────────────────────────────────────────────────


def run_mipro(
    train_examples: list,
    lms: dict[str, dspy.LM],
) -> dspy.Predict:
    """Run MIPROv2 0-shot instruction optimization."""
    print("\n" + "=" * 60)
    print("Running MIPROv2 (0-shot instruction optimization)")
    print("=" * 60)

    # Configure the target LM as default for generation
    dspy.configure(lm=lms["target"])

    mipro = dspy.MIPROv2(
        metric=composite_metric,
        auto="light",
        num_threads=4,
        max_bootstrapped_demos=0,
        max_labeled_demos=0,
        verbose=True,
    )

    optimized = mipro.compile(
        dspy.Predict(CodebaseAgentResponse),
        trainset=train_examples,
        max_bootstrapped_demos=0,
        max_labeled_demos=0,
        requires_permission_to_run=False,
    )

    return optimized


def run_gepa(
    train_examples: list,
    lms: dict[str, dspy.LM],
) -> dspy.Predict | None:
    """Run GEPA reflective evolution optimization."""
    print("\n" + "=" * 60)
    print("Running GEPA (reflective evolution)")
    print("=" * 60)

    # Configure the target LM as default for generation
    dspy.configure(lm=lms["target"])

    try:
        gepa = dspy.GEPA(
            metric=composite_metric_with_feedback,
            auto="light",
            reflection_lm=lms["reflection"],
            num_threads=4,
        )

        optimized = gepa.compile(
            dspy.Predict(CodebaseAgentResponse),
            trainset=train_examples,
        )

        return optimized

    except Exception as e:
        print(f"\nGEPA failed: {e}")
        print("Continuing with MIPROv2 results only.")
        return None


# ── Evaluation ────────────────────────────────────────────────────


def evaluate_program(
    program: dspy.Predict,
    dev_examples: list,
    lms: dict[str, dspy.LM],
    label: str,
) -> float:
    """Evaluate a program on the dev set and return average score."""
    print(f"\nEvaluating: {label}")

    dspy.configure(lm=lms["target"])

    evaluator = Evaluate(
        devset=dev_examples,
        num_threads=4,
        display_progress=True,
        provide_traceback=True,
    )

    result = evaluator(program, metric=composite_metric)
    score = float(result.score)
    print(f"  {label} score: {score:.4f}")
    return score


# ── Result extraction and saving ──────────────────────────────────


def extract_instruction(program: dspy.Predict) -> str:
    """Extract the optimized instruction text from a DSPy program."""
    return program.signature.instructions


def save_results(
    results: dict,
    optimized_programs: dict[str, dspy.Predict | None],
    timestamp: str,
) -> None:
    """Save optimization results and extracted prompts."""
    _RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    _PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    # Save the comparison summary
    summary_path = _RESULTS_DIR / f"summary_{timestamp}.json"
    summary_path.write_text(json.dumps(results, indent=2))
    print(f"\nSummary saved to {summary_path}")

    # Save optimized programs and extract prompts
    for name, program in optimized_programs.items():
        if program is None:
            continue

        # Save the full DSPy program
        program_path = _RESULTS_DIR / f"optimized_{name}_{timestamp}.json"
        program.save(str(program_path))
        print(f"Program saved to {program_path}")

        # Extract and save the optimized instruction
        instruction = extract_instruction(program)
        prompt_path = _PROMPTS_DIR / f"optimized_{name}.md"
        prompt_path.write_text(instruction + "\n")
        print(f"Prompt saved to {prompt_path}")


def print_comparison(results: dict) -> None:
    """Print a comparison table of all results."""
    print("\n" + "=" * 60)
    print("RESULTS COMPARISON")
    print("=" * 60)
    print(f"{'Program':<20} {'Dev Score':>10}")
    print("-" * 30)

    for name, score in sorted(results["scores"].items()):
        marker = " *" if score == max(results["scores"].values()) else ""
        print(f"{name:<20} {score:>10.4f}{marker}")

    print("-" * 30)
    best = max(results["scores"], key=results["scores"].get)
    print(f"Winner: {best}")

    if "instructions" in results:
        print(f"\n{'=' * 60}")
        print("OPTIMIZED INSTRUCTIONS")
        print("=" * 60)
        for name, instruction in results["instructions"].items():
            print(f"\n--- {name} ---")
            print(instruction)


# ── Main ──────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="DSPy prompt optimization for codebase-graph framing"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate setup without running optimization",
    )
    parser.add_argument(
        "--optimizer",
        choices=["mipro", "gepa", "both"],
        default="both",
        help="which optimizer to run (default: both)",
    )
    parser.add_argument(
        "--eval-only",
        action="store_true",
        help="only evaluate baseline (no optimization)",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    # Validate API key
    api_key = _get_api_key()
    lms = _configure_lms(api_key)

    # Load tasks
    print("Loading benchmark tasks...")
    train_tasks = get_train_tasks()
    dev_tasks = get_dev_tasks()
    print(f"  Train: {len(train_tasks)} tasks")
    print(f"  Dev:   {len(dev_tasks)} tasks")

    # Convert to DSPy examples
    print("Converting to DSPy examples...")
    train_examples = to_dspy_examples(train_tasks)
    dev_examples = to_dspy_examples(dev_tasks)
    print(f"  {len(train_examples)} train examples")
    print(f"  {len(dev_examples)} dev examples")

    if args.dry_run:
        print("\n--- DRY RUN ---")
        print(f"API key: {'*' * 8}...{api_key[-4:]}")
        print(f"Target LM: {lms['target'].model}")
        print(f"Judge LM: {lms['judge'].model}")
        print(f"Reflection LM: {lms['reflection'].model}")
        print(f"Baseline instruction:\n  {CodebaseAgentResponse.__doc__}")
        print(f"\nTrain example 0 task: {train_examples[0].task[:80]}...")
        print(f"Dev example 0 task: {dev_examples[0].task[:80]}...")
        print("\nDry run complete. Everything looks good.")
        return

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    results: dict = {"timestamp": timestamp, "scores": {}, "instructions": {}}
    optimized_programs: dict[str, dspy.Predict | None] = {}

    # Evaluate baseline
    print("\n--- Evaluating baseline ---")
    baseline = dspy.Predict(CodebaseAgentResponse)
    baseline_score = evaluate_program(baseline, dev_examples, lms, "baseline")
    results["scores"]["baseline"] = baseline_score
    results["instructions"]["baseline"] = extract_instruction(baseline)

    if args.eval_only:
        print_comparison(results)
        return

    # Run optimizers
    start = time.time()

    if args.optimizer in ("mipro", "both"):
        optimized_mipro = run_mipro(train_examples, lms)
        optimized_programs["mipro"] = optimized_mipro
        mipro_score = evaluate_program(optimized_mipro, dev_examples, lms, "mipro")
        results["scores"]["mipro"] = mipro_score
        results["instructions"]["mipro"] = extract_instruction(optimized_mipro)

    if args.optimizer in ("gepa", "both"):
        optimized_gepa = run_gepa(train_examples, lms)
        optimized_programs["gepa"] = optimized_gepa
        if optimized_gepa:
            gepa_score = evaluate_program(optimized_gepa, dev_examples, lms, "gepa")
            results["scores"]["gepa"] = gepa_score
            results["instructions"]["gepa"] = extract_instruction(optimized_gepa)

    elapsed = time.time() - start
    results["elapsed_seconds"] = round(elapsed, 1)
    print(f"\nOptimization took {elapsed:.1f}s")

    # Save and report
    save_results(results, optimized_programs, timestamp)
    print_comparison(results)


if __name__ == "__main__":
    main()
