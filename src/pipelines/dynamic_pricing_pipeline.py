import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn

from src.utils.utility import validate_positive_number
from src.data.data_loader import DataLoader

# --- Data Preprocessing and Validation ---
def load_and_validate_data():
    # Load raw data
    sales = DataLoader.load_csv("sales_data_dictionary.csv")
    inventory = DataLoader.load_csv("inventory_data_dictionary.csv")
    customer = DataLoader.load_csv("customer_behavior_data_dictionary.csv")
    competitor = DataLoader.load_csv("competitor_data_dictionary.csv")

    # Standardize date columns for merging
    sales = sales.rename(columns={'TransactionDate': 'Date'})
    # inventory, customer, competitor already have 'Date' column

    # Merge datasets on 'Date'
    df = sales \
        .merge(competitor, on='Date', how='left') \
        .merge(customer, on='Date', how='left') \
        .merge(inventory, on='Date', how='left')

    # Data quality checks
    assert not df.isnull().all(axis=1).any(), "Rows with all values missing detected."
    if df.isnull().sum().sum() > 0:
        df = df.dropna()  # Simple strategy; can be improved

    # Validate positive numeric columns
    for col in ['MRP', 'NoPromoPrice', 'SellingPrice', 'UnitsSold']:
        if col in df.columns:
            assert df[col].apply(validate_positive_number).all(), f"Non-positive values in {col}"

    return df

# --- Feature Engineering ---
def feature_engineering(df):
    # Price elasticity: % change in units sold / % change in price
    df['PriceElasticity'] = df['UnitsSold'].pct_change() / df['SellingPrice'].pct_change()
    # Customer engagement: combine CTR, ReturningVisitorRatio, AvgSessionDuration_sec
    df['EngagementScore'] = (
        df.get('CTR', 0).fillna(0) * 0.4 +
        df.get('ReturningVisitorRatio', 0).fillna(0) * 0.3 +
        df.get('AvgSessionDuration_sec', 0).fillna(0) * 0.3
    )
    # Inventory health: (StockEnd - SafetyStock) / Demand
    if 'StockEnd' in df.columns and 'SafetyStock' in df.columns and 'Demand' in df.columns:
        df['InventoryHealth'] = (df['StockEnd'] - df['SafetyStock']) / (df['Demand'] + 1e-5)
    # Competitor price gap
    if 'FinalPrice' in df.columns:
        df['CompetitorPriceGap'] = df['SellingPrice'] - df['FinalPrice']
    return df

# --- Model Training with Hyperparameter Optimization ---
def train_models(X_train, y_train):
    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(),
        "RandomForest": RandomForestRegressor(random_state=42)
    }
    params = {
        "Ridge": {"alpha": [0.1, 1.0, 10.0]},
        "RandomForest": {"n_estimators": [50, 100], "max_depth": [5, 10]}
    }
    best_models = {}
    for name, model in models.items():
        if name in params:
            grid = GridSearchCV(model, params[name], cv=3, scoring='neg_mean_squared_error')
            grid.fit(X_train, y_train)
            best_models[name] = grid.best_estimator_
        else:
            model.fit(X_train, y_train)
            best_models[name] = model
    return best_models

# --- Model Evaluation ---
def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    # Business metric: revenue estimation
    if 'SellingPrice' in X_test.columns and 'UnitsSold' in X_test.columns:
        revenue = (X_test['SellingPrice'] * X_test['UnitsSold']).sum()
    else:
        revenue = None
    return {"mse": mse, "mae": mae, "r2": r2, "revenue": revenue}

# --- Automated Model Selection ---
def select_best_model(results):
    # Select model with lowest MSE
    best_model = min(results, key=lambda k: results[k]['mse'])
    return best_model, results[best_model]

# --- MLflow Integration ---
def log_experiment(model_name, model, metrics, params, X_train, y_train):
    with mlflow.start_run(run_name=model_name):
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(model, model_name)
        # Optionally log sample data
        mlflow.log_artifact("data/raw/sales_data_dictionary.csv")
        mlflow.log_artifact("data/raw/inventory_data_dictionary.csv")
        mlflow.log_artifact("data/raw/customer_behavior_data_dictionary.csv")
        mlflow.log_artifact("data/raw/competitor_data_dictionary.csv")

# --- Main Pipeline ---
def main():
    # Load and preprocess data
    df = load_and_validate_data()
    df = feature_engineering(df)

    # Define features and target
    feature_cols = [col for col in df.columns if col not in ['SellingPrice', 'Date']]
    X = df[feature_cols]
    y = df['SellingPrice']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train models
    best_models = train_models(X_train, y_train)

    # Evaluate and compare models
    results = {}
    for name, model in best_models.items():
        metrics = evaluate_model(model, X_test, y_test)
        results[name] = metrics
        log_experiment(name, model, metrics, model.get_params() if hasattr(model, "get_params") else {}, X_train, y_train)

    # Select best model
    best_model_name, best_metrics = select_best_model(results)
    print(f"Best model: {best_model_name} with metrics: {best_metrics}")

if __name__ == "__main__":
    main()