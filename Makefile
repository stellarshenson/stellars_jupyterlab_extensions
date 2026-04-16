# Makefile for Stellars JupyterLab Extensions metapackage version 1.1
# changelog:
#   1.1 - add mrproper target for deep cleanup (dist, build, caches, venv)
#   1.0 - initial versioned Makefile

.PHONY: clean build install uninstall publish help increment_version mrproper

help:
	@echo "Available targets:"
	@echo "  clean             - Remove build artifacts"
	@echo "  mrproper          - Deep clean (clean + caches + venv)"
	@echo "  increment_version - Increment patch version"
	@echo "  build             - Build the package (increments version)"
	@echo "  install           - Install the package locally (increments version)"
	@echo "  uninstall         - Uninstall the package"
	@echo "  publish           - Publish to PyPI (increments version)"

clean:
	rm -rf dist/ build/ *.egg-info/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

increment_version:
	@CURRENT=$$(grep -Po '(?<=^version = ")[^"]+' pyproject.toml); \
	MAJOR=$$(echo $$CURRENT | cut -d. -f1); \
	MINOR=$$(echo $$CURRENT | cut -d. -f2); \
	PATCH=$$(echo $$CURRENT | cut -d. -f3); \
	NEW_PATCH=$$((PATCH + 1)); \
	NEW_VERSION="$$MAJOR.$$MINOR.$$NEW_PATCH"; \
	sed -i "s/^version = \"$$CURRENT\"/version = \"$$NEW_VERSION\"/" pyproject.toml; \
	sed -i "s/^__version__ = \"$$CURRENT\"/__version__ = \"$$NEW_VERSION\"/" stellars_jupyterlab_extensions/__init__.py; \
	echo "Version incremented: $$CURRENT -> $$NEW_VERSION"

build: increment_version clean
	pip install build
	python -m build

install: increment_version clean
	pip install build
	python -m build
	pip install dist/*.whl

uninstall:
	pip uninstall -y stellars_jupyterlab_extensions

publish: increment_version clean
	pip install build
	python -m build
	pip install twine
	twine upload dist/*

mrproper: clean
	rm -rf dist/ build/ *.egg-info/ .venv || true
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
