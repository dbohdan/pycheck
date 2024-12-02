# pycheck

This POSIX shell script runs
[Ruff](https://github.com/astral-sh/uv)
and
[Pyright](https://github.com/microsoft/pyright)
using
[uv](https://github.com/astral-sh/uv)
to format, lint, and type-check (in that order) your standalone Python scripts.

## Requirements

A system that can run uv and POSIX shell scripts.

## Installation

First, install uv.
Assuming you have `~/.local/bin/` directory in `PATH`, run the following commands:

```shell
uv run --with 'httpx[cli]' httpx --download pycheck https://raw.githubusercontent.com/dbohdan/pycheck/refs/heads/master/pycheck
chmod +x pycheck
mv pycheck ~/.local/bin/
```

## License

MIT.
