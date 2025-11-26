# Makefile for Stellars JupyterLab Extensions metapackage version 1.0

.PHONY: clean build install uninstall publish help

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build artifacts"
	@echo "  build     - Build the package"
	@echo "  install   - Install the package locally"
	@echo "  uninstall - Uninstall the package"
	@echo "  publish   - Publish to PyPI (requires TWINE_USERNAME and TWINE_PASSWORD)"

clean:
	rm -rf dist/ build/ *.egg-info/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

build: clean
	pip install build
	python -m build

install: build
	pip install dist/*.whl

uninstall:
	pip uninstall -y stellars_jupyterlab_extensions

publish: build
	pip install twine
	twine upload dist/*
