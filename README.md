# Devops-Bottleneck-Analyser
# DevOps Team Productivity and Bottleneck Analyzer

This project analyzes development and deployment metrics to detect productivity bottlenecks in a DevOps workflow using machine learning. It identifies inefficiencies and provides actionable recommendations to improve team throughput and software delivery.

---

## 🚀 Features

- Load DevOps metrics from an Excel file
- Perform trend analysis on build, deploy, review, and issue resolution times
- Detect workflow bottlenecks using Isolation Forest (unsupervised ML)
- Generate optimization recommendations based on anomaly insights
- Visualize productivity metrics using line graphs

---

## 📁 Project Structure
Devops-Bottleneck-Analyser/
│
├── main.py
│   └── 🔁 Runs the full analysis pipeline:
│       ├── Loads data from → data/devops_metrics.xlsx
│       ├── Performs trend analysis
│       ├── Detects bottlenecks (ML - Isolation Forest)
│       ├── Recommends improvements
│       └── Plots visual insights
│
├── requirements.txt
│   └── 📦 Lists dependencies (pandas, sklearn, matplotlib, openpyxl)
│
├── README.md
│   └── 📘 Instructions, usage, and project overview
│
├── .gitignore
│   └── ❌ Excludes unnecessary files (.pyc, __pycache__, .env, etc.)
│
└── data/
    └── devops_metrics.xlsx
        └── 📊 Input dataset (100+ records of DevOps performance metrics)
