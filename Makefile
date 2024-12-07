.PHONY: default
default: shellcheck

.PHONY: shellcheck
shellcheck:
	shellcheck pycheck
