SHELL		:= /bin/bash

VENV_DIR    := ./.venv
VENV_BIN    := $(VENV_DIR)/bin
PYTHONPATH	:= $$PYTHONPATH:$(shell pwd)

PY_BASE	    := /usr/bin/python3.6
PY	    	:= $(PYTHONPATH) $(VENV_BIN)/python
PIP	    	:= $(VENV_BIN)/pip
VAULT	    := $(VENV_BIN)/ansible-vault


venv-create:
	@test ! -d $(VENV_DIR) && \
	$(PY_BASE) -m venv $(VENV_DIR) || \
	echo "Virtualenv already exists."

venv-destroy:
	@rm -rf $(VENV_DIR)

deps-install: venv-create
	@$(PIP) install -r requirements.txt

vault-decrypt:
	@$(VAULT) decrypt --output=secrets app_envs

app-start:
	@source secrets; $(PY) src/main.py
