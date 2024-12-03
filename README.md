# pycheck

This POSIX shell script runs
[Ruff](https://github.com/astral-sh/uv)
and
[Pyright](https://github.com/microsoft/pyright)
using
[uv](https://github.com/astral-sh/uv)
to format, lint, and type-check (in that order) your standalone Python scripts.
It doesn't require a project and doesn't create cache directories like `.ruff_cache`.

## Requirements

A system that can run uv and POSIX shell scripts.

## Installation

First, [install uv](https://github.com/astral-sh/uv#installation).

Assuming you have the directory `~/.local/bin/` in `PATH`, run the following commands:

```shell
uv run --with 'httpx[cli]' httpx --download pycheck https://raw.githubusercontent.com/dbohdan/pycheck/refs/heads/master/pycheck
chmod +x pycheck
mv pycheck ~/.local/bin/
```

## Usage

```none
Usage: pycheck [-h] [-V] [-f] [-i <rules>] [-t <version>] [-u] file [file ...]

Options:
  -h, --help
          Print this help message and exit

  -V, --version
          Print version number and exit

  -f, --fix
          Apply Ruff Linter fixes

  -i, --ignore <rules>
          Ruff Linter rules to ignore (default: 'ANN,D,EXE003,PT,S101,S310,S603,S607,T201')

  -t, --target-version <version>
          Target Python version (default: '3.10')

  -u, --unsafe-fixes
          Apply unsafe Ruff Linter fixes
```

## License

MIT.
