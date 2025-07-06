# churn_service/predictor.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os
import logging

logging.basicConfig(level=logging.INFO)

def train_model(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    logging.info("Model training complete.")
    return clf

def evaluate_model(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    logging.info("Model evaluation report:\n" + report)
    return report

def save_model(clf, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(clf, path)
    logging.info(f"Model saved to {path}")

def load_model(path):
    clf = joblib.load(path)
    logging.info(f"Model loaded from {path}")
    return clf
