# ml/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def load_data():
    path = os.path.join('data', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
    df = pd.read_csv(path)
    return df

def preprocess(df):
    # Drop customerID
    df = df.drop('customerID', axis=1)

    # Convert target
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Encode categorical columns
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col])

    return df

def train_and_save(df):
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    os.makedirs('models', exist_ok=True)
    joblib.dump(clf, 'models/model.pkl')

if __name__ == "__main__":
    df = load_data()
    df = preprocess(df)
    train_and_save(df)
