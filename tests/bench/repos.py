"""Benchmark repository management.

Clones and cleans up real OSS repos used as fixtures for prompt
optimization benchmarks.
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from pathlib import Path

log = logging.getLogger(__name__)

BENCHMARK_REPOS = [
    {"name": "fastapi", "url": "https://github.com/tiangolo/fastapi.git"},
    {"name": "express", "url": "https://github.com/expressjs/express.git"},
    {"name": "solid", "url": "https://github.com/solidjs/solid.git"},
    {"name": "flask", "url": "https://github.com/pallets/flask.git"},
]


def clone_repo(repo_info: dict[str, str], target_dir: Path) -> Path:
    """Shallow-clone a repo into target_dir/<name>.

    Returns the path to the cloned directory.
    Raises subprocess.CalledProcessError on failure.
    """
    dest = target_dir / repo_info["name"]
    log.info("Cloning %s -> %s", repo_info["url"], dest)
    subprocess.run(
        ["git", "clone", "--depth", "1", repo_info["url"], str(dest)],
        check=True,
        capture_output=True,
        text=True,
    )
    return dest


def cleanup_repo(path: Path) -> None:
    """Remove a cloned repo directory."""
    if path.exists():
        shutil.rmtree(path)
        log.info("Removed %s", path)


def clone_all(base_dir: Path) -> dict[str, Path]:
    """Clone all benchmark repos. Returns {name: path} for successful clones."""
    results: dict[str, Path] = {}
    for repo in BENCHMARK_REPOS:
        try:
            path = clone_repo(repo, base_dir)
            results[repo["name"]] = path
        except subprocess.CalledProcessError as exc:
            log.error("Failed to clone %s: %s", repo["name"], exc.stderr)
    return results
