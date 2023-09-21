.PHONY: clean
clean: clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -rf build dist .eggs
	find . -name '*.egg-info' -exec rm -rf  {} +
	find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

.PHONY: install
install: clean
	poetry install

.PHONY: lint
lint: install
	poetry run pre-commit run --all-files
	poetry run python3 -c 'from generate_version import test; test()'

.PHONY: release
release: dist ## package and upload a release
	poetry publish -r "$$POETRY_REPOSITORY" ## set by CDP overlay


.PHONY: dist
dist: clean ## builds source and wheel package
	poetry build

.PHONY: version
version:
	git fetch --tags --verbose
	poetry version "$$(poetry run python3 ./generate_version.py)"
