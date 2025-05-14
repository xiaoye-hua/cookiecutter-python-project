.PHONY: help test clean update-rules

help:
	@echo "Available commands:"
	@echo "  make test         - Run all tests"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make update-rules - Update cursor rules from upstream"

test:
	pytest tests/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf build/ dist/ *.egg-info .coverage htmlcov/

update-rules:
	git submodule update --remote
	git add .cursor/rules
	git commit -m "Update cursor rules to latest version"
