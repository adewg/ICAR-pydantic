#!/usr/bin/env sh

BASEDIR=$(dirname $0)
cd "$BASEDIR"
cd ../ICAR-schema/scripts
chmod +x schema_bundle.sh
./schema_bundle.sh
