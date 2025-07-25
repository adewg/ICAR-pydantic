#!/usr/bin/env sh

cd scripts
./main.py
pre-commit run -a -v || true
