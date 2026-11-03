# Student Performance Predictor — Beginner Python Script
# Converted from the uploaded Jupyter Notebook.
# Run from project folder: python train_model.py
# Required CSV: data/student_performance_data.csv

# Student Performance Predictor
# Beginner-friendly notebook. Run cells from top to bottom. We predict current_mark using attendance, previous_mark, and assignment_mark. All records are synthetic.

# =================================================================
# SECTION 1 — Import libraries
# =================================================================
# pandas reads data; matplotlib draws charts; scikit-learn trains and evaluates the model; joblib saves it.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from pathlib import Path
import joblib


# =================================================================
# SECTION 2 — Load the CSV
# =================================================================
# Keep the notebook in the main project folder. The CSV is inside the data folder.

data_path = Path("data") / "student_performance_data.csv"
df = pd.read_csv(data_path)
print(df.head())


# =================================================================
# SECTION 3 — Understand the dataset
# =================================================================
# Check row count, column types and summary statistics.

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.info())
print(df.describe())


# =================================================================
# SECTION 4 — Check data quality
# =================================================================
# Missing values and duplicates can affect results. Here we inspect them and remove rows with missing values and exact duplicates.

print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
df = df.dropna().drop_duplicates().copy()
print("Rows remaining:", len(df))


# =================================================================
# SECTION 5 — Visualize the marks
# =================================================================
# A histogram shows how the current marks are distributed.

df["current_mark"].hist(bins=15)
plt.xlabel("Current mark")
plt.ylabel("Number of students")
plt.title("Distribution of current marks")
plt.show()


# =================================================================
# SECTION 6 — Look at relationships
# =================================================================
# A correlation table describes how numerical columns tend to move together. Correlation does not prove causation.

print(df.corr(numeric_only=True).round(2))
pd.plotting.scatter_matrix(df, figsize=(9, 9))
plt.tight_layout()
plt.show()


# =================================================================
# SECTION 7 — Choose inputs and target
# =================================================================
# X contains the three known inputs; y contains the mark we want to predict. Never include the target inside X.

feature_names = ["attendance", "previous_mark", "assignment_mark"]
X = df[feature_names]
y = df["current_mark"]
print(X.head())
print(y.head())


# =================================================================
# SECTION 8 — Split into training and test data
# =================================================================
# 80% of records teach the model; 20% are held back to check predictions on unseen records. random_state=42 makes the split reproducible.

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))


# =================================================================
# SECTION 9 — Train Linear Regression
# =================================================================
# Linear Regression learns a simple relationship between the three inputs and current mark.

model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained!")


# =================================================================
# SECTION 10 — Evaluate the model
# =================================================================
# MAE is the average absolute difference between predictions and actual marks. R² compares the model with predicting the mean test mark.

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"MAE: {mae:.2f} marks")
print(f"R²: {r2:.3f}")
results = pd.DataFrame({"Actual": y_test.to_numpy(), "Predicted": predictions})
print(results.head(10))


# =================================================================
# SECTION 11 — Compare actual and predicted marks
# =================================================================
# Dots closer to the diagonal indicate smaller errors.

plt.scatter(y_test, predictions, alpha=0.7)
plt.plot([0, 100], [0, 100], linestyle="--", color="gray")
plt.xlabel("Actual current mark")
plt.ylabel("Predicted current mark")
plt.title("Actual vs predicted")
plt.show()


# =================================================================
# SECTION 12 — Predict one new student
# =================================================================
# Create one row with the same input column names. The values below are just an example.

new_student = pd.DataFrame([{
    "attendance": 85,
    "previous_mark": 70,
    "assignment_mark": 80,
}])
mark = model.predict(new_student)[0]
mark = max(0, min(100, mark))
print(f"Estimated current mark: {mark:.1f}/100")


# =================================================================
# SECTION 13 — Save the model
# =================================================================
# The predict.py program will load this file. Only load .pkl files you trust.

model_path = Path("models") / "student_model.pkl"
model_path.parent.mkdir(exist_ok=True)
joblib.dump(model, model_path)
print("Saved to:", model_path)

# What to try next
# Change the example student values, compare MAE with another model, and eventually test using appropriately collected real student data. Synthetic-data accuracy is not evidence of real-world accuracy.
