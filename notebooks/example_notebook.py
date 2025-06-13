# Contents of /azure-ml-databricks-ml-project/azure-ml-databricks-ml-project/notebooks/example_notebook.py

import pandas as pd
import matplotlib.pyplot as plt
from src.data_preprocessing import load_data, clean_data
from src.model_training import ModelTrainer

# Load raw data
data = load_data('data/raw/data_file.csv')

# Clean the data
cleaned_data = clean_data(data)

# Display basic statistics
print(cleaned_data.describe())

# Visualize the data
plt.figure(figsize=(10, 6))
plt.hist(cleaned_data['column_of_interest'], bins=30, alpha=0.7)
plt.title('Distribution of Column of Interest')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Initialize model trainer
trainer = ModelTrainer()

# Train the model
model = trainer.train_model(cleaned_data)

# Save the model
trainer.save_model(model, 'models/trained_model.pkl')