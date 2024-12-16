import pandas as pd
import numpy as np
from data_preprocessing import load_and_preprocess_data
from feature_scaling import scale_features
from model_selection import train_classifiers
from evaluation import evaluate_model, plot_confusion_matrix

def main():
    # Load and preprocess the data
    data, target = load_and_preprocess_data('data/UNSW-NB15_1.csv')
    
    # Scale features
    X_scaled, y = scale_features(data, target)
    
    # Train classifiers and get results
    results = train_classifiers(X_scaled, y)
    
    # Evaluate models
    for model_name, (y_test, y_pred) in results.items():
        print(f"Evaluating {model_name}")
        evaluate_model(y_test, y_pred)
        plot_confusion_matrix(y_test, y_pred, classes=np.unique(y))

if __name__ == "__main__":
    main()