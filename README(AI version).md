# Local Project Context MCP Server

This repository contains a compact Python MCP server for inspecting a local project without modifying it. Built with FastMCP, `server.py` exposes an `inspect_project_context` tool that reports the project root, Git branch, sanitized remotes, working-tree status, and a deterministic file inventory capped at 200 entries; it also excludes common environment, cache, and Git directories. The project targets FastMCP 4.x through the single dependency declared in `requirements.txt`.

The repository also includes reusable Codex skill definitions, including a read-only natural-English checker and an HW8 greeting test, with copies organized under `.codex/skills/` for local discovery. Supporting files document setup and demonstrations, while `.gitignore` keeps virtual environments, Python bytecode, caches, and macOS metadata out of version control.

PS: This "Readme.md" is created to test the MCP, it's not the real readme!!!!
