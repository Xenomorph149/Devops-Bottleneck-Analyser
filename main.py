# DevOps Team Productivity and Bottleneck Analyzer
import json
import pandas as pd
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

# --- Real Data Loader ---
def load_real_metrics(file_path="data/devops_metrics.xlsx"):
    df = pd.read_excel(file_path, parse_dates=['date'])
    df.rename(columns={'date': 'timestamp'}, inplace=True)
    return df

# --- Workflow Analyzer ---
def analyze_trends(df):
    print("--- Trend Analysis ---")
    for col in df.columns[1:-1]:
        print(f"{col} average: {df[col].mean():.2f}, std dev: {df[col].std():.2f}")

# --- Bottleneck Detector ---
def detect_bottlenecks(df):
    print("--- Bottleneck Detection ---")
    model = IsolationForest(contamination=0.1)
    numeric_df = df.select_dtypes(include=[np.number])
    df['score'] = model.fit_predict(numeric_df)
    anomalies = df[df['score'] == -1]
    print(f"Detected {len(anomalies)} potential bottlenecks.")
    return anomalies

# --- Recommendation Engine ---
def recommend_improvements(df, anomalies):
    print("--- Recommendations ---")
    if len(anomalies) > 0:
        for col in df.columns[1:-2]:
            if pd.api.types.is_numeric_dtype(df[col]):
                avg_anomaly = anomalies[col].mean()
                avg_overall = df[col].mean()
                if avg_anomaly > avg_overall * 1.3:
                    print(f"Suggestion: Optimize {col} (anomalies show ~30% higher duration)")
    else:
        print("No bottlenecks detected. Workflow appears optimal.")

# --- Visualization ---
def plot_metrics(df):
    df.set_index('timestamp')[['build_duration', 'deploy_duration', 'code_review_time', 'issue_resolution_time']].plot(figsize=(12, 6))
    plt.title("DevOps Productivity Metrics Over Time")
    plt.xlabel("Date")
    plt.ylabel("Duration (minutes")
    plt.tight_layout()
    plt.show()

# --- Main Pipeline ---
def main():
    df = load_real_metrics("data/devops_metrics.xlsx")
    analyze_trends(df)
    anomalies = detect_bottlenecks(df)
    recommend_improvements(df, anomalies)
    plot_metrics(df)

if __name__ == '__main__':
    main()
