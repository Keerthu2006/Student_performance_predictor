from flask import Flask, render_template, request, jsonify, send_from_directory
import joblib
import pandas as pd
import json
import os

app = Flask(__name__)

# Load model and scaler globally
try:
    model = joblib.load('best_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not scaler:
        return jsonify({'error': 'Model not loaded on server.'}), 500
        
    try:
        data = request.json
        features = ['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignments', 'Internal_Marks']
        
        # Extract features in the correct order
        input_data = [[
            float(data['Study_Hours']),
            float(data['Attendance']),
            float(data['Previous_Marks']),
            float(data['Assignments']),
            float(data['Internal_Marks'])
        ]]
        
        df = pd.DataFrame(input_data, columns=features)
        scaled_data = scaler.transform(df)
        prediction = model.predict(scaled_data)[0]
        
        result = "Pass" if prediction == 1 else "Fail"
        return jsonify({'prediction': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/metrics', methods=['GET'])
def get_metrics():
    try:
        with open('metrics.json', 'r') as f:
            metrics = json.load(f)
        return jsonify(metrics)
    except FileNotFoundError:
        return jsonify({'error': 'metrics.json not found. Train models first.'}), 404

@app.route('/plots/<filename>')
def serve_plot(filename):
    return send_from_directory('plots', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
