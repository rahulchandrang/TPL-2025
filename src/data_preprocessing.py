def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(df):
    # Example cleaning steps
    df = df.dropna()  # Remove missing values
    df = df.drop_duplicates()  # Remove duplicates
    return df

def transform_data(df):
    # Example transformation steps
    # Convert categorical variables to dummy variables
    df = pd.get_dummies(df)
    return df

def preprocess_data(file_path):
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    processed_data = transform_data(cleaned_data)
    return processed_data