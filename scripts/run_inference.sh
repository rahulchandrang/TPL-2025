#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Load environment variables
export $(cat .env | xargs)

# Run the inference script
python src/inference/predict.py --input data/processed/input_data.csv --output data/processed/predictions.csv

# Deactivate the virtual environment
deactivate