"""FastMCP server that exposes read-only local project context."""

from __future__ import annotations

import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from fastmcp import FastMCP


PROJECT_ROOT = Path(__file__).resolve().parent
IGNORED_DIRECTORIES = {".git", ".venv", ".venv-fastmcp", "__pycache__"}
MAX_FILES = 200

# stdout is reserved for the MCP stdio protocol. All diagnostics go to stderr.
logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

mcp = FastMCP("Local Project Context")


def _run_git(*args: str) -> tuple[bool, str]:
    """Run a read-only Git command and return its success state and output."""
    try:
        result = subprocess.run(
            ["git", "-C", str(PROJECT_ROOT), *args],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return False, str(exc)

    output = result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
    return result.returncode == 0, output


def _sanitize_remote(url: str) -> str:
    """Remove credentials embedded in an HTTP(S) Git remote."""
    return re.sub(r"(https?://)[^/@]+@", r"\1", url)


def _list_project_files() -> tuple[list[str], bool]:
    """Return a bounded, deterministic inventory of project files."""
    files: list[str] = []
    for path in sorted(PROJECT_ROOT.rglob("*")):
        if any(part in IGNORED_DIRECTORIES for part in path.relative_to(PROJECT_ROOT).parts):
            continue
        if not path.is_file() or path.name == ".DS_Store":
            continue
        files.append(path.relative_to(PROJECT_ROOT).as_posix())
        if len(files) >= MAX_FILES:
            return files, True
    return files, False


@mcp.tool
def inspect_project_context() -> dict[str, Any]:
    """Inspect the current local project before editing, debugging, documenting, or forming repository URLs.

    Use this tool when you need reliable project context instead of guessing from a
    partial prompt or screenshot. It returns the project root, current Git branch,
    sanitized remotes, concise working-tree status, and a bounded file inventory.
    The operation is read-only, performs no network requests, and never changes files.
    """
    files, files_truncated = _list_project_files()
    inside_repo, repo_check = _run_git("rev-parse", "--is-inside-work-tree")

    git_context: dict[str, Any] = {"is_repository": inside_repo and repo_check == "true"}
    if git_context["is_repository"]:
        branch_ok, branch = _run_git("branch", "--show-current")
        remotes_ok, remotes_text = _run_git("remote", "-v")
        status_ok, status_text = _run_git("status", "--short")

        remote_lines = []
        if remotes_ok and remotes_text:
            remote_lines = [_sanitize_remote(line) for line in remotes_text.splitlines()]

        git_context.update(
            {
                "branch": branch if branch_ok and branch else "detached-or-unborn",
                "remotes": remote_lines,
                "status": status_text.splitlines() if status_ok and status_text else [],
            }
        )
    else:
        git_context["error"] = repo_check or "Not a Git repository"

    return {
        "project_root": str(PROJECT_ROOT),
        "git": git_context,
        "files": files,
        "files_truncated": files_truncated,
        "file_limit": MAX_FILES,
    }


if __name__ == "__main__":
    mcp.run()
