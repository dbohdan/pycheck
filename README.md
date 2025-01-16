# pycheck

This Python script runs
[Ruff](https://github.com/astral-sh/uv)
and
[Pyright](https://github.com/microsoft/pyright)
using
[uv](https://github.com/astral-sh/uv)
to format, lint, and type-check (in that order) your standalone Python scripts.
It doesn't require a project and doesn't create cache directories like `.ruff_cache`.

## Requirements

You will need uv.
As of late 2024, it supports Linux, macOS, and Windows.
See [platform support](https://docs.astral.sh/uv/reference/policies/platforms/) for uv.

## Installation

First, [install uv](https://github.com/astral-sh/uv#installation).
Once it is installed, run the following command:

```shell
uv tool install git+https://github.com/dbohdan/pycheck@master
```

## Usage

```none
usage: pycheck [-h] [-V] [-f] [-i <rules>] [-t <version>] [-u] file [file ...]

Run Ruff and Pyright with uv to format, lint, and type-check Python scripts.

positional arguments:
  file                  File to check

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -f, --fix             apply Ruff Linter fixes
  -i <rules>, --ignore <rules>
                        Ruff Linter rules to ignore (default:
'ANN,D,EXE003,PT,S101,S310,S603,S607,T201'; '+...' to add)
  -t <version>, --target-version <version>
                        target Python version (default: '3.10')
  -u, --unsafe-fixes    apply unsafe Ruff Linter fixes
```

## License

MIT.
