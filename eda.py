import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_eda():
    if not os.path.exists('student_data.csv'):
        print("Dataset not found. Run data_generator.py first.")
        return

    df = pd.read_csv('student_data.csv')
    
    # Create directory for plots
    os.makedirs('plots', exist_ok=True)
    
    # Display basic info
    print("Dataset Information:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Fill missing values for EDA plots
    df_clean = df.fillna(df.median(numeric_only=True))
    
    sns.set_theme(style="whitegrid")
    
    # Plot 1: Study hours vs marks
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df_clean, x='Study_Hours', y='Previous_Marks', hue='Final_Result', palette='Set1')
    plt.title('Study Hours vs Previous Marks')
    plt.savefig('plots/study_vs_marks.png')
    plt.close()
    
    # Plot 2: Attendance vs Result
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df_clean, x='Final_Result', y='Attendance', palette='Set2')
    plt.title('Attendance Distribution by Result')
    plt.savefig('plots/attendance_vs_result.png')
    plt.close()
    
    # Plot 3: Grade Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df_clean, x='Grade', order=['A', 'B', 'C', 'F'], palette='viridis')
    plt.title('Distribution of Grades')
    plt.savefig('plots/grade_distribution.png')
    plt.close()
    
    # Plot 4: Correlation Matrix
    plt.figure(figsize=(10, 8))
    numeric_df = df_clean.select_dtypes(include=['float64', 'int64']).drop(columns=['Student_ID'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Feature Correlation Matrix')
    plt.savefig('plots/correlation_matrix.png')
    plt.close()
    
    print("EDA completed. Plots saved in the 'plots' directory.")

if __name__ == '__main__':
    run_eda()
