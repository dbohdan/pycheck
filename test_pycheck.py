#! /usr/bin/env python3

import os
import subprocess as sp
import unittest
from pathlib import Path

DIR = Path(__file__).parent
PYTHON_TARGET_VERSION = "3.10"
SCRIPT = os.getenv("PYCHECK", "./pycheck")


def pycheck(*args: str) -> sp.CompletedProcess:
    return sp.run(
        [SCRIPT, *args],
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
        self.assertIn("Usage:", result.stdout)

    def test_version(self) -> None:
        result = pycheck("-V")
        self.assertEqual(result.returncode, 0)
        self.assertIn("0.2.0", result.stdout)

    def test_no_files(self) -> None:
        result = pycheck()
        self.assertEqual(result.returncode, 2)
        self.assertIn("no files given", result.stderr)

    def test_unknown_option(self) -> None:
        result = pycheck("--unknown-option")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown option", result.stderr)

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
