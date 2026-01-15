SHELL := /bin/bash

.PHONY: setup setup-posix setup-windows

setup:
	@uname | grep -qiE 'mingw|msys|cygwin' && $(MAKE) setup-windows || $(MAKE) setup-posix

setup-posix:
	@chmod +x setup_scripts/bootstrap.sh
	@./setup_scripts/bootstrap.sh
	@echo ""
	@echo "Activate with: source .venv/bin/activate"

setup-windows:
	@pwsh setup_scripts/bootstrap.ps1
	@echo ""
	@echo "Activate with: .venv\\Scripts\\Activate.ps1"
