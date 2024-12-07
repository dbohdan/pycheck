PYTHON_VERSION := 3.10

.PHONY: default
default: check test

.PHONY: check
check:
	uv run --python $(PYTHON_VERSION) pycheck.py pycheck.py test_pycheck.py

.PHONY: test
test:
	uv run --python $(PYTHON_VERSION) test_pycheck.py
