import pandas as pd
import numpy as np

def generate_data(num_students=500):
    np.random.seed(42)
    
    student_ids = np.arange(1, num_students + 1)
    
    # Generate features
    study_hours = np.random.uniform(0, 10, num_students)
    attendance = np.random.uniform(30, 100, num_students)
    previous_marks = np.random.uniform(20, 100, num_students)
    assignments = np.random.uniform(30, 100, num_students)
    internal_marks = np.random.uniform(10, 50, num_students) # max 50
    
    # Add some noise and create a target variable based on inputs
    # A simple linear combination with noise to simulate realistic data
    score = (0.2 * (study_hours / 10 * 100) + 
             0.2 * attendance + 
             0.3 * previous_marks + 
             0.1 * assignments + 
             0.2 * (internal_marks / 50 * 100) + 
             np.random.normal(0, 10, num_students))
    
    # Determine Pass/Fail (Threshold: 50)
    final_result = np.where(score >= 50, 'Pass', 'Fail')
    
    # Determine Grades based on score
    def get_grade(s):
        if s >= 80: return 'A'
        elif s >= 60: return 'B'
        elif s >= 50: return 'C'
        else: return 'F'
        
    grades = [get_grade(s) for s in score]
    
    df = pd.DataFrame({
        'Student_ID': student_ids,
        'Study_Hours': np.round(study_hours, 1),
        'Attendance': np.round(attendance, 1),
        'Previous_Marks': np.round(previous_marks, 1),
        'Assignments': np.round(assignments, 1),
        'Internal_Marks': np.round(internal_marks, 1),
        'Grade': grades,
        'Final_Result': final_result
    })
    
    # Introduce a few missing values to allow data preprocessing steps
    missing_indices = np.random.choice(num_students, size=15, replace=False)
    df.loc[missing_indices[:5], 'Study_Hours'] = np.nan
    df.loc[missing_indices[5:10], 'Attendance'] = np.nan
    df.loc[missing_indices[10:], 'Previous_Marks'] = np.nan
    
    df.to_csv('student_data.csv', index=False)
    print(f"Dataset generated with {num_students} records: student_data.csv")
    print(df.head())

if __name__ == '__main__':
    generate_data(1000)
