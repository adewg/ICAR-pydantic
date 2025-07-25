#!/usr/bin/env sh

cd scripts
./main.py
# first time should fail and its normal
pre-commit run -a || true
# second time should succeed so we must be sure to catch any remaining errors
pre-commit run -a -v
