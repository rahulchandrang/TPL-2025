import pytest
import pandas as pd
from src.features.feature_engineering import create_features

def test_create_features():
    raw_data = pd.DataFrame({
        'price': [10, 20, 30],
        'demand': [100, 200, 300],
        'season': ['summer', 'winter', 'spring']
    })
    
    features = create_features(raw_data)
    
    assert 'feature_1' in features.columns
    assert 'feature_2' in features.columns
    assert features.shape[0] == raw_data.shape[0]
    assert features['feature_1'].dtype == 'float64'
    assert features['feature_2'].dtype == 'int64'