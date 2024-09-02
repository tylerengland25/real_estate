# Variables
PYTHON=python3
PIP=pip3
VENV=backend/venv
REQUIREMENTS=backend/requirements.txt
BACKEND_SRC_DIR=backend/src
BACKEND_TEST_DIR=backend/tests
FRONTEND_DIR=frontend

# Help
.PHONY: help
help:
    @echo "Usage: make [target]"
    @echo ""
    @echo "Targets:"
    @echo "  help            Display this help message"
    @echo "  venv            Create a virtual environment for the backend"
    @echo "  install         Install backend dependencies"
    @echo "  run-backend     Run the backend data pipeline"
    @echo "  test-backend    Run backend tests"
    @echo "  clean-backend   Clean up the backend environment"
    @echo "  install-frontend Install frontend dependencies"
    @echo "  start-frontend  Start the frontend development server"
    @echo "  build-frontend  Build the frontend for production"
    @echo "  clean-frontend  Clean up the frontend environment"

# Backend
.PHONY: venv
venv:
    $(PYTHON) -m venv $(VENV)

.PHONY: install
install: venv
    $(VENV)/bin/$(PIP) install -r $(REQUIREMENTS)

.PHONY: run-backend
run-backend: install
    $(VENV)/bin/$(PYTHON) $(BACKEND_SRC_DIR)/data_pipeline.py

.PHONY: test-backend
test-backend: install
    $(VENV)/bin/$(PYTHON) -m unittest discover $(BACKEND_TEST_DIR)

.PHONY: clean-backend
clean-backend:
    rm -rf $(VENV)
    find . -type f -name '*.pyc' -delete
    find . -type d -name '__pycache__' -delete

# Frontend
.PHONY: install-frontend
install-frontend:
    cd $(FRONTEND_DIR) && npm install

.PHONY: start-frontend
start-frontend:
    cd $(FRONTEND_DIR) && npm start

.PHONY: build-frontend
build-frontend:
    cd $(FRONTEND_DIR) && npm run build

.PHONY: clean-frontend
clean-frontend:
    rm -rf $(FRONTEND_DIR)/node_modules
    rm -rf $(FRONTEND_DIR)/build