# Data Structure and Documentation for Tide Dynamic Pricing Model

## Data Directory Structure

The data directory is organized into two main subdirectories:

- **raw/**: This directory contains the raw data files used for training and testing the model. These files are in their original format and have not undergone any preprocessing.

- **processed/**: This directory holds the processed data files that are ready for analysis and modeling. The files in this directory have been cleaned, transformed, and are structured for use in the machine learning pipeline.

## Data Sources

The raw data files are sourced from [insert data source here, e.g., internal databases, public datasets, etc.]. Ensure that you have the necessary permissions to access and use this data.

## Preprocessing Steps

1. **Data Cleaning**: Remove any duplicates, handle missing values, and correct inconsistencies in the data.
2. **Feature Engineering**: Transform raw data into features suitable for modeling. This includes creating new variables, normalizing data, and encoding categorical variables.
3. **Data Splitting**: The processed data will be split into training, validation, and test sets to evaluate model performance effectively.

## Usage

To load the raw and processed data, utilize the `DataLoader` class defined in `src/data/data_loader.py`. This class provides methods to load datasets from the respective directories.

For further details on feature creation and model training, refer to the relevant scripts in the `src/features` and `src/models` directories.