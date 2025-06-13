import pytest
from src.features.build_features import build_features

def test_build_features():
    # Add your test data and expected output here
    raw_data = ...
    expected_features = ...

    # Call the build_features function
    features = build_features(raw_data)

    # Assert that the features match the expected output
    assert features == expected_features

def test_build_features_edge_case():
    # Test edge cases for the build_features function
    edge_case_data = ...
    expected_edge_case_features = ...

    features = build_features(edge_case_data)

    assert features == expected_edge_case_features