import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib
import json

def main():
    print("Loading data...")
    try:
        df = pd.read_csv('student_data.csv')
    except FileNotFoundError:
        print("Error: student_data.csv not found. Run data_generator.py first.")
        return

    # Data Preprocessing
    print("Preprocessing data...")
    # Handle missing values by imputing with median
    features = ['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignments', 'Internal_Marks']
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].median())
        
    # Convert categorical target to binary (Pass/Fail -> 1/0)
    le = LabelEncoder()
    df['Final_Result_Encoded'] = le.fit_transform(df['Final_Result']) # Assuming Pass is 1, Fail is 0 (check mapping)
    
    # Let's explicitly map Pass to 1 and Fail to 0
    df['Final_Result_Encoded'] = df['Final_Result'].apply(lambda x: 1 if x == 'Pass' else 0)

    # Feature Selection
    X = df[features]
    y = df['Final_Result_Encoded']

    # Splitting data (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalization / Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save the scaler for future predictions
    joblib.dump(scaler, 'scaler.pkl')

    # Model Selection
    models = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Naive Bayes': GaussianNB(),
        'SVM': SVC(random_state=42)
    }

    best_model = None
    best_accuracy = 0
    best_model_name = ""
    
    all_metrics = {}

    print("\n--- Model Training & Evaluation ---")
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        cm = confusion_matrix(y_test, y_pred)
        
        all_metrics[name] = {
            "Accuracy": float(acc),
            "Precision": float(prec),
            "Recall": float(rec),
            "F1_Score": float(f1),
            "Confusion_Matrix": cm.tolist()
        }
        
        print(f"\n{name} Results:")
        print(f"Accuracy:  {acc:.4f}")
        print(f"Precision: {prec:.4f}")
        print(f"Recall:    {rec:.4f}")
        print(f"F1-Score:  {f1:.4f}")
        print("Confusion Matrix:")
        print(cm)
        
        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model
            best_model_name = name

    print(f"\nBest Model: {best_model_name} with Accuracy: {best_accuracy:.4f}")
    
    # Save the best model
    joblib.dump(best_model, 'best_model.pkl')
    print(f"Saved {best_model_name} to best_model.pkl")
    
    with open('metrics.json', 'w') as f:
        json.dump(all_metrics, f, indent=4)
    print("Saved metrics to metrics.json")

if __name__ == '__main__':
    main()
