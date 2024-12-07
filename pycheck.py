#! /usr/bin/env -S uv run --no-project --python 3.10
"""
pycheck - Run Ruff and Pyright with uv to format, lint, and type-check
standalone Python scripts.

Copyright (c) 2024 D. Bohdan.
License: MIT.
See https://github.com/dbohdan/pycheck for more information.
"""

import argparse
import subprocess as sp
import sys

DEFAULT_IGNORE_RULES = "ANN,D,EXE003,PT,S101,S310,S603,S607,T201"
DEFAULT_TARGET_VERSION = "3.10"
VERSION = "0.3.0"


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run Ruff and Pyright with uv to "
            "format, lint, and type-check Python scripts."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=VERSION,
    )

    parser.add_argument(
        "-f",
        "--fix",
        action="store_true",
        help="apply Ruff Linter fixes",
    )

    parser.add_argument(
        "-i",
        "--ignore",
        default=DEFAULT_IGNORE_RULES,
        metavar="<rules>",
        help="Ruff Linter rules to ignore (default: %(default)r; '+...' to add)",
    )

    parser.add_argument(
        "-t",
        "--target-version",
        default=DEFAULT_TARGET_VERSION,
        metavar="<version>",
        help="target Python version (default: %(default)r)",
    )

    parser.add_argument(
        "-u",
        "--unsafe-fixes",
        action="store_true",
        help="apply unsafe Ruff Linter fixes",
    )

    parser.add_argument(
        "files",
        metavar="file",
        nargs="+",
        help="File to check",
    )

    return parser.parse_args()


def main() -> None:
    args = cli()

    target_version_ruff = f"py{args.target_version.replace('.', '')}"

    ruff_format_command = [
        "uv",
        "tool",
        "run",
        "ruff",
        "format",
        "--no-cache",
        "--target-version",
        target_version_ruff,
        *args.files,
    ]

    ignore = (
        DEFAULT_IGNORE_RULES + "," + args.ignore[1:]
        if args.ignore.startswith("+")
        else args.ignore
    )
    ruff_check_command = [
        "uv",
        "tool",
        "run",
        "ruff",
        "check",
        "--ignore",
        ignore,
        "--no-cache",
        "--select",
        "ALL",
        "--target-version",
        target_version_ruff,
        *args.files,
    ]
    if args.fix:
        ruff_check_command.append("--fix")
    if args.unsafe_fixes:
        ruff_check_command.append("--unsafe-fixes")

    pyright_command = [
        "uv",
        "tool",
        "run",
        "pyright",
        "--pythonversion",
        args.target_version,
        *args.files,
    ]

    status = 0
    for command in (ruff_format_command, ruff_check_command, pyright_command):
        result = sp.run(command, check=False)
        status = max(status, result.returncode)

    sys.exit(status)


if __name__ == "__main__":
    main()
