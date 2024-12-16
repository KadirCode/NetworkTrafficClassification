# NetworkTrafficClassification
This project aims to develop a machine learning model to classify network traffic by application type based on TCP/IP packet features. The implementation includes data preprocessing, feature scaling, model training using various classifiers, and evaluation of model performance.

Project Overview
As internet traffic grows, classifying network applications (e.g., HTTP, FTP) is crucial for effective management and security. This project leverages the UNSW-NB15 Network Traffic Dataset to build and evaluate machine learning models for network traffic classification.

Objectives
Build a classifier to identify network application types.
Analyze feature importance to understand application traffic patterns.
Methodology
Data Preprocessing: Load data, select relevant features, clean and encode variables.
Feature Scaling: Normalize features for consistent model input.
Model Selection: Train classifiers like Decision Trees, Random Forests, and K-Nearest Neighbors.
Evaluation: Use metrics (accuracy, precision, recall, F1-score) and a confusion matrix for analysis.
Tools and Libraries
Programming: Python
Libraries: Pandas, Scikit-Learn, Matplotlib, Seaborn
