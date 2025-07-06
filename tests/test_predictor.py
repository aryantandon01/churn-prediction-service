# tests/test_predictor.py

from churn_service.predictor import train_model
from sklearn.datasets import make_classification

def test_train_model():
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    clf = train_model(X, y)
    assert clf is not None
    assert hasattr(clf, "predict")

