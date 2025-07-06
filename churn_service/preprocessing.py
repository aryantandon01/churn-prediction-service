# churn_service/preprocessing.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import logging

logging.basicConfig(level=logging.INFO)

def load_data(path):
    logging.info(f"Loading data from {path}")
    df = pd.read_csv(path)
    return df

def preprocess(df):
    logging.info("Starting preprocessing...")
    df = df.drop('customerID', axis=1)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col])

    logging.info("Preprocessing completed.")
    return df
