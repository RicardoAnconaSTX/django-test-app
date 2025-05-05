.PHONY: lint format check

# Run ruff for linting
lint:
	ruff check .

# Auto-format code with black and fix with ruff
format:
	black .
	ruff check . --fix

# Combine lint and format checks (no fixing)
check:
	black --check .
	ruff check .

fix:
	ruff check . --select W292 --fix