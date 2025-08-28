#!/usr/bin/env bash

BASEDIR=$(dirname $0)
cd "$BASEDIR"
cd ..
datamodel-codegen \
  --input ./ICAR-schema/bundled-schemes/combinedURLScheme.json \
  --input-file-type openapi \
  --use-schema-description \
  --collapse-root-models \
  --custom-template-dir ./custom_templates \
  --output-model-type pydantic_v2.BaseModel \
  --output ./tmp/raw_models.py
