#!/usr/bin/env sh

BASEDIR=$(dirname $0)
cd "$BASEDIR"
cd ..
datamodel-codegen --input ./ICAR/bundled-schemes/combinedURLScheme.json --input-file-type openapi --output ./tmp/raw_model.py
