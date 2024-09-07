# Variables
PYTHON=python3
PIP=pip3
BACKEND_PATH=backend
VENV=venv
REQUIREMENTS=requirements.txt

# Help
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help            Show this help message"
	@echo "  setup            Create and activate virtual environment"

# Create virtual environment
.PHONY: venv
venv:
	@if [ ! -d $(VENV) ]; then \
		$(PYTHON) -m venv $(BACKEND_PATH)/$(VENV); \
	fi
	@$(BACKEND_PATH)/$(VENV)/bin/$(PIP) install --upgrade pip
	@$(BACKEND_PATH)/$(VENV)/bin/$(PIP) install -r $(BACKEND_PATH)/$(REQUIREMENTS)

.PHONY: pre-commit
pre-commit: venv
	@$(BACKEND_PATH)/$(VENV)/bin/pre-commit install

# Install dependencies
.PHONY: setup
setup: venv pre-commit
