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
	@echo "  venv            Create and activate virtual environment"

# Create virtual environment
.PHONY: setup_venv
setup_venv:
	@if [ ! -d $(VENV) ]; then \
		$(PYTHON) -m venv $(BACKEND_PATH)/$(VENV); \
	fi
	@$(BACKEND_PATH)/$(VENV)/bin/$(PIP) install --upgrade pip

# Install dependencies
.PHONY: venv
venv: setup_venv
	@$(BACKEND_PATH)/$(VENV)/bin/$(PIP) install -r $(BACKEND_PATH)/$(REQUIREMENTS)