PYTHON_VERSION := 3.10

.PHONY: default
default: shellcheck test

.PHONY: shellcheck
shellcheck:
	shellcheck pycheck

.PHONY: test
test:
	uv run --python $(PYTHON_VERSION) test_pycheck.py
