# Student Performance Prediction System

## 1. Title of the Project
Student Performance Prediction System using Machine Learning

This project predicts student academic performance based on factors like attendance, study hours, previous grades, and socio-economic background. Machine learning models such as Logistic Regression, Decision Trees, Naive Bayes, and Support Vector Machines (SVM) are used to analyze the data.

**Objective**: Identify students at risk of failing to take preventive actions.
**Dataset**: Student academic records
**Tech Stack**: Python, Pandas, Matplotlib, Seaborn, Scikit-learn
**Outcome**: Helps institutions take preventive actions and improve overall academic outcomes using data-driven insights.

## 2. Problem Statement
In traditional education systems:
- Teachers cannot easily track individual student performance trends.
- Early identification of weak students is difficult.
- Decisions are based on intuition rather than data.

This project aims to automate performance prediction using historical student data.

## 3. Technologies Used
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib
- **Tools**: Excel/CSV (Dataset)

## 4. System Architecture
1. **Data Collection**: Generated a synthetic student dataset (`data_generator.py`).
2. **Data Preprocessing**: Handled missing values, encoded categorical data, and normalized numerical values.
3. **Exploratory Data Analysis (EDA)**: Visualized relationships (e.g., Study hours vs marks, Attendance vs result) (`eda.py`).
4. **Feature Selection**: Selected important features: Study Hours, Attendance, Previous Marks, Assignments, Internal Marks.
5. **Model Training**: Applied multiple ML algorithms (Logistic Regression, Decision Tree, Naive Bayes, SVM) and split data (80% Train, 20% Test) (`train_models.py`).
6. **Prediction Output**: Input new student data and predict Pass/Fail output (`predict.py`).
7. **Performance Evaluation**: Evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

## 5. How to Run the Project

1. **Install Dependencies**:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn joblib
   ```

2. **Generate the Dataset**:
   Run the following command to generate the `student_data.csv` file.
   ```bash
   python data_generator.py
   ```

3. **Run Exploratory Data Analysis (EDA)**:
   This will generate plots and save them in the `plots/` directory.
   ```bash
   python eda.py
   ```

4. **Train the Models**:
   This script will train all models, evaluate them, and save the best performing model (`best_model.pkl`) and scaler (`scaler.pkl`).
   ```bash
   python train_models.py
   ```

5. **Make Predictions**:
   Run this script to predict performance on new sample student data.
   ```bash
   python predict.py
   ```

## 6. Expected Output
- **Model Evaluation**: Metrics printed to the console comparing Accuracy, Precision, Recall, and F1-Score for each model.
- **Graphs**: EDA visualizations stored in the `plots/` folder showing trends.
- **Predictions**: A final list of students predicted to fail, highlighting at-risk students for early intervention.

## 7. Advantages
- Early detection of weak students
- Improves teaching strategies
- Data-driven decision making
- Saves time for teachers

## 8. Limitations
- Requires quality dataset (model is as good as the data).
- Cannot capture emotional/psychological factors.

## 9. Future Enhancements
- Integration with mobile app or Learning Management Systems (LMS).
- Real-time performance tracking.
- AI-based personalized learning recommendations.
