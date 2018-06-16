PY			= $(VENV_BIN)/python
PIP			= $(VENV_BIN)/pip
PY_BASE	    := python3.6
VENV_DIR    := ./.venv
VENV_BIN	:= $(VENV_DIR)/bin


venv-create:
	@test ! -d $(VENV_DIR) && $(PY_BASE) -m venv $(VENV_DIR) || echo "Virtualenv already exists."

venv-destroy:
	@rm -rf $(VENV_DIR)

deps-install: venv-create
	@pip install -r requirements.txt
