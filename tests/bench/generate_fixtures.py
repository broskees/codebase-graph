"""Generate .codebase.md fixtures from real OSS repos.

Run as: python -m tests.bench.generate_fixtures

For each benchmark repo:
1. Shallow-clone to a temp directory
2. Run codebase-graph oneshot to produce .codebase.md
3. Copy the result to tests/bench/fixtures/{name}.codebase.md
4. Clean up the clone
"""

from __future__ import annotations

import logging
import re
import shutil
import tempfile
from pathlib import Path

from tests.bench.repos import BENCHMARK_REPOS, cleanup_repo, clone_repo

log = logging.getLogger(__name__)

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _generate_one(repo_info: dict[str, str], clone_dir: Path) -> Path | None:
    """Clone a repo, run oneshot, return the fixture path (or None on failure)."""
    from src.cli import run_oneshot

    name = repo_info["name"]
    repo_path: Path | None = None

    try:
        repo_path = clone_repo(repo_info, clone_dir)
        log.info("Running oneshot index for %s ...", name)

        run_oneshot(repo_path)

        generated = repo_path / ".codebase.md"
        if not generated.exists():
            log.error("%s: .codebase.md was not created", name)
            return None

        dest = FIXTURES_DIR / f"{name}.codebase.md"
        shutil.copy2(generated, dest)
        log.info("%s: fixture written to %s", name, dest)
        return dest

    except Exception:
        log.exception("Failed to generate fixture for %s", name)
        return None

    finally:
        if repo_path is not None:
            cleanup_repo(repo_path)


def _print_summary(fixture_path: Path) -> None:
    """Print a quick summary of a generated fixture."""
    content = fixture_path.read_text()
    chars = len(content)
    token_est = chars // 4

    symbol_count = 0
    module_count = 0

    match = re.search(r"symbols\[(\d+)\]", content)
    if match:
        symbol_count = int(match.group(1))

    match = re.search(r"modules\[(\d+)\]", content)
    if match:
        module_count = int(match.group(1))

    has_toon = "```toon" in content

    print(
        f"  {fixture_path.name}: "
        f"{module_count} modules, {symbol_count} symbols, "
        f"~{token_est} tokens, toon={'yes' if has_toon else 'NO'}"
    )


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )

    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)

    generated: list[Path] = []
    failed: list[str] = []

    with tempfile.TemporaryDirectory(prefix="bench_repos_") as tmp:
        clone_dir = Path(tmp)
        for repo in BENCHMARK_REPOS:
            result = _generate_one(repo, clone_dir)
            if result is not None:
                generated.append(result)
            else:
                failed.append(repo["name"])

    print(f"\nGenerated {len(generated)}/{len(BENCHMARK_REPOS)} fixtures:")
    for path in generated:
        _print_summary(path)

    if failed:
        print(f"\nFailed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
