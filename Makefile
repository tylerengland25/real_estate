# Variables
PYTHON=python3
PIP=pip3
VENV=venv
REQUIREMENTS=requirements.txt

# Help
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help            Show this help message"
	@echo "  setup           Create and activate virtual environment"

# Create virtual environment
.PHONY: venv
venv:
	@if [ ! -d $(VENV) ]; then \
		$(PYTHON) -m venv $(VENV); \
	fi
	@$(VENV)/bin/$(PIP) install --upgrade pip
	@$(VENV)/bin/$(PIP) install -r $(REQUIREMENTS)

.PHONY: pre-commit
pre-commit: venv
	@$(VENV)/bin/pre-commit install

# Install dependencies
.PHONY: setup
setup: venv pre-commit
