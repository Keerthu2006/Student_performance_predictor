import pandas as pd
import joblib

def predict_performance(data):
    try:
        model = joblib.load('best_model.pkl')
        scaler = joblib.load('scaler.pkl')
    except FileNotFoundError:
        print("Model or scaler not found. Run train_models.py first.")
        return

    # Expected features in this order
    features = ['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignments', 'Internal_Marks']
    
    # Ensure data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data, columns=features)
        
    scaled_data = scaler.transform(data)
    predictions = model.predict(scaled_data)
    
    # Map back to Pass/Fail
    results = ['Pass' if p == 1 else 'Fail' for p in predictions]
    
    data['Predicted_Result'] = results
    return data

if __name__ == '__main__':
    # Sample new student data
    new_students = [
        [8.5, 95.0, 88.0, 90.0, 45.0], # Likely Pass
        [2.0, 45.0, 40.0, 50.0, 20.0], # Likely Fail
        [5.0, 70.0, 60.0, 65.0, 30.0], # Borderline
    ]
    
    print("Evaluating new student data...")
    results_df = predict_performance(new_students)
    
    if results_df is not None:
        print("\nPredictions:")
        print(results_df)
        
        at_risk = results_df[results_df['Predicted_Result'] == 'Fail']
        if not at_risk.empty:
            print("\nAlert: The following students are at risk of failing:")
            print(at_risk)
        else:
            print("\nAll students are predicted to pass.")
