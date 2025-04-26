#!/bin/bash
# Save as convert_to_html.sh

# Set variables
NOTEBOOK="code/q1.ipynb"
OUTPUT_DIR="../output"
OUTPUT_FILE="q1.html"

# Convert and save to the output directory
jupyter nbconvert --to html --execute "$NOTEBOOK" --output="$OUTPUT_DIR/$OUTPUT_FILE"

echo "Converted notebook saved to: $OUTPUT_DIR/$OUTPUT_FILE"

# Set variables
NOTEBOOK="code/q2_4.ipynb"
OUTPUT_DIR="../output"
OUTPUT_FILE="q2_4.html"

# Convert and save to the output directory
jupyter nbconvert --to html --execute "$NOTEBOOK" --output="$OUTPUT_DIR/$OUTPUT_FILE"

echo "Converted notebook saved to: $OUTPUT_DIR/$OUTPUT_FILE"

# Set variables
NOTEBOOK="code/q3_5.ipynb"
OUTPUT_DIR="../output"
OUTPUT_FILE="q3_5.html"

# Convert and save to the output directory
jupyter nbconvert --to html --execute "$NOTEBOOK" --output="$OUTPUT_DIR/$OUTPUT_FILE"

echo "Converted notebook saved to: $OUTPUT_DIR/$OUTPUT_FILE"

# Set variables
NOTEBOOK="code/q6_7.ipynb"
OUTPUT_DIR="../output"
OUTPUT_FILE="q6_7.html"

# Convert and save to the output directory
jupyter nbconvert --to html --execute "$NOTEBOOK" --output="$OUTPUT_DIR/$OUTPUT_FILE"

echo "Converted notebook saved to: $OUTPUT_DIR/$OUTPUT_FILE"

