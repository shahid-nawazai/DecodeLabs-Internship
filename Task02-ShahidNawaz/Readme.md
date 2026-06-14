# Iris Flower Classification using K-Nearest Neighbors (KNN)

This repository contains a Python implementation of a machine learning pipeline that classifies Iris flowers into three species (*Setosa*, *Versicolor*, and *Virginica*) based on their sepal and petal measurements. The project utilizes Scikit-Learn to build a K-Nearest Neighbors (KNN) classifier.

## Performance Summary

The model achieved flawless performance on the test split:
* **Accuracy:** 100% (`1.0`)
* **Weighted F1-Score:** 1.0

---

## Pipeline Architecture

The script implements a complete end-to-end Machine Learning workflow:

1. **Dataset Loading:** Imports the classic Iris dataset containing 150 samples with 4 features each.
2. **Feature Scaling:** Uses `StandardScaler` to normalize features by removing the mean and scaling to unit variance. This is crucial for distance-based algorithms like KNN.
3. **Data Splitting:** Divides the data into an 80% training set and a 20% testing set (shuffled with a fixed `random_state=42` for reproducibility).
4. **Model Training:** Initialized a `KNeighborsClassifier` with $k = 5$ neighbors and fits it to the scaled training data.
5. **Evaluation:** Evaluates the model using a confusion matrix and classification report.
6. **Inference:** Accepts a raw sample, applies the learned scaling transformations, and predicts its species.

---

