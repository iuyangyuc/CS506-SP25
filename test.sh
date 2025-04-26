#!/bin/bash
# Save as convert_to_html.sh

# Set variables
NOTEBOOK="code/test.ipynb"
OUTPUT_DIR="../output"
OUTPUT_FILE="test.html"

# Convert and save to the output directory
jupyter nbconvert --to html --execute "$NOTEBOOK" --output="$OUTPUT_DIR/$OUTPUT_FILE"

echo "Converted notebook saved to: $OUTPUT_DIR/$OUTPUT_FILE"