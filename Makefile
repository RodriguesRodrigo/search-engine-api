all: help

help:
	@echo ""
	@echo "Usage: make COMMAND"
	@echo ""
	@echo "Commands:"
	@echo "  help			List all commands"
	@echo "  install		Install all dependencies from the project"
	@echo "  run			Start the application"
	@echo "  setup			Run virtualenv and install Commands"
	@echo "  virtualenv		Create virtualenv to install dependencies"

virtualenv:
	python -m venv venv

	@echo ""
	@echo "# IMPORTANT!"
	@echo "# Please start your virtualenv with 'source venv/bin/activate'"
	@echo "# To exit from virtualenv just run 'deactivate'"

install:
	pip install -r requirements.txt; \
	pip install -e .; \

setup:
	@echo "# Creating virtualenv and installing all dependencies"
	@echo ""

	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	pip install -e .; \

	@echo ""
	@echo "# IMPORTANT!"
	@echo "# Please start your virtualenv with 'source venv/bin/activate' to run the project."

run:
	python application.py
