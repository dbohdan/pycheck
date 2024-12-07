#! /usr/bin/env python3

import os
import shlex
import subprocess as sp
import sys
import unittest
from pathlib import Path

DIR = Path(__file__).parent
PYTHON_TARGET_VERSION = "3.10"

PYCHECK_COMMAND = shlex.split(os.getenv("PYCHECK_COMMAND", ""))
if not PYCHECK_COMMAND:
    PYCHECK_COMMAND = [sys.executable, "pycheck.py"]


def pycheck(*args: str) -> sp.CompletedProcess:
    return sp.run(
        [*PYCHECK_COMMAND, *args],
        check=False,
        capture_output=True,
        text=True,
    )


class TestPycheck(unittest.TestCase):
    def setUp(self) -> None:
        os.chdir(DIR)

    def test_help(self) -> None:
        result = pycheck("-h")
        self.assertEqual(result.returncode, 0)
        self.assertIn("usage:", result.stdout)

    def test_version(self) -> None:
        result = pycheck("-V")
        self.assertEqual(result.returncode, 0)
        self.assertRegex(result.stdout, r"^\d.\d+.\d+")

    def test_no_files(self) -> None:
        result = pycheck()
        self.assertEqual(result.returncode, 2)
        self.assertIn("arguments are required: file", result.stderr)

    def test_unknown_option(self) -> None:
        result = pycheck("--unknown-option", "foo.py")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unrecognized arguments", result.stderr)

    def test_ignore_option(self) -> None:
        result = pycheck("-i", "ALL", "test_pycheck.py")
        self.assertEqual(result.returncode, 0)

    def test_ignore_option_error(self) -> None:
        result = pycheck("-i", "NOPE", "test_pycheck.py")
        self.assertNotEqual(result.returncode, 0)

    def test_target_version_option(self) -> None:
        result = pycheck("-t", PYTHON_TARGET_VERSION, "test_pycheck.py")
        self.assertEqual(result.returncode, 0)

    def test_check_errors(self) -> None:
        result = pycheck("foo.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertRegex(result.stdout, r"Found \d+ errors\.")


if __name__ == "__main__":
    unittest.main()
