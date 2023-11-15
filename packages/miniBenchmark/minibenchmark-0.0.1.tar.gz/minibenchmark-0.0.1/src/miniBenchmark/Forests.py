import numpy as np
from sklearn.ensemble import IsolationForest

def IF(X, n_jobs, random_state=42):
    

    # Initialize IsolationForest with the contamination parameter set to 0.05
    iso_forest = IsolationForest(contamination=0.05, n_jobs=-1, random_state=random_state)

    # Fit the model
    iso_forest.fit(X)

    # Predict if a data point is an outlier (-1 for outliers and 1 for inliers)
    outlier_pred = iso_forest.predict(X)

    # Select all rows that are not outliers (inliers)
    X_clean = X[outlier_pred == 1]

    # If you have a corresponding target array y, clean it as well
    # y_clean = y[outlier_pred == 1]

    # X_clean now contains your cleaned data without the outliers
    return X



from sklearn.ensemble import RandomForestClassifier

def RF(X, y, n_jobs=-1, random_state=42):
    """
    Trains a Random Forest classifier on the provided data.

    Parameters:
    - X: numpy array or pandas DataFrame, feature data for training the model.
    - y: numpy array or pandas Series, target labels for supervised learning.
    - n_jobs: int, number of parallel jobs to run (-1 to use all available cores).
    - random_state: int, seed for the random number generator.

    Returns:
    - rf_model: trained Random Forest classifier.
    - feature_importances_: array of feature importances.
    """

    # Initialize RandomForestClassifier
    rf_model = RandomForestClassifier(n_jobs=n_jobs, random_state=random_state)

    # Fit the model
    rf_model.fit(X, y)

    # Get feature importances
    feature_importances = rf_model.feature_importances_

    return rf_model, feature_importances

# Example usage:
# Assuming X is your feature matrix and y is the label vector
# rf_model, feature_importances = RF(X, y)

from .generate_data_tasks import generate_dataset


def task_rf_all(size):
    # Example usage:
# Assuming X is your feature matrix and y is the label vector
    
    ids, X, y = generate_dataset(M=size, n=30, task='classification', random_state=42)


    rf_model, feature_importances = RF(X, y, n_jobs=-1)

def task_if_all(size):
    # Example usage:
# Assuming X is your feature matrix and y is the label vector
    
    ids, X, y = generate_dataset(M=size, n=30, task='classification', random_state=42)


    IF(X, n_jobs=-1)


#task_rf_all(2**18)
#task_if_all(2**22)
#https://github.com/scikit-learn/scikit-learn/issues/12469
