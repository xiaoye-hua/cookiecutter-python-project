.PHONY: help test clean update-cursor-rules push-cursor-rule-edits

help:
	@echo "Available commands:"
	@echo "  make test                 - Run all tests"
	@echo "  make clean                - Remove build artifacts"
	@echo "  make update-cursor-rules  - Pull latest cursor rules from remote"
	@echo "  make push-cursor-rule-edits - Push local cursor rule changes to remote"

test:
	pytest tests/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf build/ dist/ *.egg-info .coverage htmlcov/

# Pull latest version of the cursor rules from the remote rule repo
update-cursor-rules:
	git submodule update --remote --merge
	git add .cursor/rules
	git commit -m "Update cursor rule pack to latest version"

# Push any changes made to the cursor rules from this project back to the cursor-rules repository
push-cursor-rule-edits:
	cd .cursor/rules && \
	git checkout main && \
	git add . && \
	git commit -m "Edit cursor rules from $$(basename $$(git rev-parse --show-toplevel))" && \
	git push origin main && \
	cd ../.. && \
	git add .cursor/rules && \
	git commit -m "Track updated cursor rule pointer"
