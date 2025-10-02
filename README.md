# KNN Classification & Regression Projects

This project demonstrates the use of **K-Nearest Neighbors (KNN)** for both **classification** and **regression** tasks.

---

## 1. KNN Classification

- **Dataset:** Breast Cancer Wisconsin Dataset (`sklearn.datasets`)
- **Goal:** Predict whether a tumor is **malignant** or **benign**.
- **Method:** K-Nearest Neighbors Classifier
- **Steps:**
  1. Load and explore the dataset
  2. Split data into training and test sets
  3. Scale features using StandardScaler
  4. Train the KNN classifier
  5. Make predictions and evaluate accuracy

---

## 2. KNN Regression

- **Dataset:** Custom-created dataset
- **Goal:** Predict continuous numerical values
- **Method:** K-Nearest Neighbors Regressor
- **Steps:**
  1. Create a dataset (`x` and `y` values)
  2. Split data into training and test sets
  3. Train the KNN regression model
  4. Make predictions and evaluate performance (e.g., MSE or R²)

---

## 3. Usage

1. Clone the repository:
```bash
git clone <repo-link>
```

Install the required libraries:
```bash
pip install -r requirements.txt
```

Run the Python scripts:
```bash
python knn_classification.py
python knn_regression.py
```
4. Results

Classification: The model successfully classifies tumors as malignant or benign.
Regression: The model can predict numerical values in the custom dataset.

5. Requirements

Python 3.x
scikit-learn
numpy
pandas (optional, for data handling)
matplotlib / seaborn (optional, for visualization)




