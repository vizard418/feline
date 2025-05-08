#!/bin/bash
source "$FELINE_DIR/.venv/bin/activate"
python "$FELINE_DIR/feline.py" "$@"
deactivate