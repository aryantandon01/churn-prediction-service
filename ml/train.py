# ml/train.py

from churn_service.preprocessing import load_data, preprocess
from churn_service.predictor import train_model, evaluate_model, save_model
from churn_service.config import DATA_PATH, MODEL_PATH
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    df = load_data(DATA_PATH)
    df = preprocess(df)

    X = df.drop('Churn', axis=1)
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    clf = train_model(X_train, y_train)
    evaluate_model(clf, X_test, y_test)
    save_model(clf, MODEL_PATH)
