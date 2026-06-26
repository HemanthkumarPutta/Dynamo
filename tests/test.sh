#!/bin/bash

# Ensure output directories exist
mkdir -p /logs/verifier

# Run pytest using CTRF reporting configuration (no runtime dependencies are installed here)
pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA

# Set final reward state in correct Harbor path
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi