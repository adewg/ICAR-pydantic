#!/usr/bin/env bash

# Get the script directory and project root
SCRIPT_DIR=$(dirname "$0")
PROJECT_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)
ICAR_SCRIPTS_DIR="$PROJECT_ROOT/ICAR-schema/scripts"

echo "Script directory: $SCRIPT_DIR"
echo "Project root: $PROJECT_ROOT"
echo "ICAR scripts directory: $ICAR_SCRIPTS_DIR"

# Check if ICAR-schema directory exists
if [ ! -d "$PROJECT_ROOT/ICAR-schema" ]; then
    echo "Error: ICAR-schema directory not found at $PROJECT_ROOT/ICAR-schema"
    echo "Please ensure the ICAR schema repository is cloned in the project root."
    exit 1
fi

# Check if the schema bundle script exists
if [ ! -f "$ICAR_SCRIPTS_DIR/schema_bundle.sh" ]; then
    echo "Error: schema_bundle.sh not found at $ICAR_SCRIPTS_DIR/schema_bundle.sh"
    exit 1
fi

# Make the script executable and run it
chmod +x "$ICAR_SCRIPTS_DIR/schema_bundle.sh"

# Change to the ICAR scripts directory and run the bundle script
cd "$ICAR_SCRIPTS_DIR"
echo "Running schema bundle from: $(pwd)"

# Run with bash to ensure compatibility
bash ./schema_bundle.sh
