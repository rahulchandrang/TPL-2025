#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Load environment variables
export $(cat .env | xargs)

# Run the training script
python src/models/train.py

# Deactivate the virtual environment
deactivate