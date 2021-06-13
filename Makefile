all: help

help:
	@echo ""
	@echo "Usage: make COMMAND"
	@echo ""
	@echo "Commands:"
	@echo "  clean			Clean all dependencies from pip and others"
	@echo "  help			List all commands"
	@echo "  install		Install all dependencies from the project"
	@echo "  run			Start the application"
	@echo "  setup			Run virtualenv and install Commands"
	@echo "  test			Run tests with coverage"
	@echo "  virtualenv		Create virtualenv to install dependencies"

virtualenv:
	python -m venv venv

	@echo ""
	@echo "# IMPORTANT!"
	@echo "# Please start your virtualenv with 'source venv/bin/activate'"
	@echo "# To exit from virtualenv just run 'deactivate'"

install:
	pip install -r requirements.txt; \
	pip install -r requirements-dev.txt; \
	pip install -e .; \

setup:
	@echo "# Creating virtualenv and installing all dependencies"
	@echo ""

	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	pip install -r requirements-dev.txt; \
	pip install -e .; \

	@echo ""
	@echo "# IMPORTANT!"
	@echo "# Please start your virtualenv with 'source venv/bin/activate' to run the project."

run:
	python app.py

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e . --upgrade --no-cache

test:
	pytest tests/ -v --cov=application
