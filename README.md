# 🎓 Student Performance Predictor

### Machine Learning Project | Python • Scikit-learn • Pandas

An end-to-end beginner machine learning project that predicts a student's examination mark using historical academic indicators.

The project demonstrates data preprocessing, exploratory data analysis, Linear Regression, model evaluation, prediction, and model persistence.

**Project Type:** Machine Learning / Regression  
**Language:** Python 3.11  
**Model:** Linear Regression  
**Status:** Completed educational prototype

> **Important:** This project uses synthetic student records. Evaluation results demonstrate model behaviour on artificial data, not real-world predictive accuracy.

---

## 🚀 Key Features

- Built a Linear Regression model using Scikit-learn.
- Analysed student performance data using Pandas.
- Handled missing values and duplicate records.
- Visualised distributions and relationships using Matplotlib.
- Used an 80/20 training and testing split.
- Evaluated predictions using Mean Absolute Error (MAE) and R².
- Saved the trained model using Joblib.
- Developed an interactive command-line prediction interface with input validation.

## 🧠 How It Works

The model uses three input features:

| Feature | Description |
|---|---|
| `attendance` | Student attendance percentage (0–100) |
| `previous_mark` | Previous examination mark (0–100) |
| `assignment_mark` | Assignment mark (0–100) |

**Prediction target:** `current_mark`, the estimated current examination mark out of 100.

### Machine Learning Workflow

```text
Synthetic Student Dataset
          |
          v
Data Exploration and Cleaning
          |
          v
Feature and Target Selection
          |
          v
Training / Test Split (80/20)
          |
          v
Linear Regression Training
          |
          v
Evaluation (MAE and R²)
          |
          v
Save Trained Model
          |
          v
Command-Line Prediction
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data processing |
| Matplotlib | Data visualisation |
| Scikit-learn | Model training and evaluation |
| Joblib | Model persistence |

## 📂 Project Structure

```text
Student-Performance-Predictor/
├── data/
│   └── student_performance_data.csv
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
└── models/                 # Created during training
    └── student_model.pkl
```

The dataset should be stored inside the `data/` directory before training.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/justlivingwith007-tech/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```

### 2. Create a Python virtual environment

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
```

### 3. Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Train the model

Make sure `data/student_performance_data.csv` exists.

```powershell
.\.venv\Scripts\python.exe train_model.py
```

The script performs data exploration, cleans the dataset, trains the model, calculates evaluation metrics and saves the trained model.

Some visualisations open in separate windows. Close each plot window to continue execution.

The resulting model is saved to:

```text
models/student_model.pkl
```

### 5. Make a prediction

```powershell
.\.venv\Scripts\python.exe predict.py
```

Enter the requested attendance, previous mark, and assignment mark. Each input must be a number between 0 and 100.

The program displays an estimated examination mark.

## 📊 Model Evaluation

The project evaluates Linear Regression on a held-out test set.

| Metric | Purpose |
|---|---|
| MAE | Average absolute prediction error, measured in marks |
| R² | Measures predictive performance relative to a mean-prediction baseline |

The training script prints the evaluation results and displays an actual-versus-predicted scatter plot.

**Recorded test results:** Add the actual MAE and R² printed by `train_model.py` after reproducing training.

The model is evaluated using synthetic data, so these metrics should not be interpreted as evidence of performance on real students.

## 💻 Prediction Example

The prediction interface asks for:

```text
Attendance percentage (0-100):
Previous mark (0-100):
Assignment mark (0-100):
```

After valid inputs are entered, it displays an estimated mark between 0 and 100.

## ⚠️ Limitations

- The dataset contains synthetic records.
- Linear Regression assumes an additive linear relationship between input features and the target.
- Model evaluation uses a single train/test split rather than cross-validation.
- Input features do not capture every factor influencing academic achievement.
- The project has not been validated on real-world student records.
- Predictions should not be used for high-stakes educational decisions.

## 🔮 Future Improvements

- Add automated unit tests with Pytest.
- Compare Linear Regression with alternative regression models.
- Introduce cross-validation.
- Add feature importance or coefficient interpretation.
- Add a Streamlit interface.
- Evaluate using appropriately collected, permissioned real-world data.

## 👨‍💻 About the Developer

**Aswin Balasubramanian**

MSc Artificial Intelligence student at the University of Leicester, United Kingdom.

Interested in AI engineering, machine learning, predictive modelling and practical software development.

Seeking **2027 UK AI/ML internships and industrial placements**.

**GitHub:** https://github.com/justlivingwith007-tech

**LinkedIn:** https://www.linkedin.com/in/aswin-balasubramanian-10b1aa321/

---

*An educational machine learning project demonstrating foundational skills in Python, regression, data analysis and model evaluation.*
