# Student Performance Predictor (Beginner Project)

This project predicts a student's **current examination mark** (0–100) using:
- attendance (percentage)
- previous_mark (out of 100)
- assignment_mark (out of 100)

The included dataset has **synthetic student records**. Results on this artificial dataset do not demonstrate real-world prediction accuracy.

## Files
- `data/student_performance_data.csv` — example student records
- `train_model.ipynb` — learn data analysis, model training and evaluation step by step
- `predict.py` — enter values to predict a mark after training
- `requirements.txt` — libraries to install
- `models/` — trained model is saved here after running the notebook

## How to run (VS Code or terminal)
1. Open the `Student_Performance_Predictor` folder in VS Code.
2. Open a terminal in this folder.
3. Create a virtual environment: `python -m venv .venv`
4. Install libraries: `python -m pip install -r requirements.txt` (or use `.venv` Python after activation).
5. Select the Python interpreter from `.venv` in VS Code.
6. Open `train_model.ipynb` and run the cells **in order**, top to bottom.
7. Once `models/student_model.pkl` exists, run `python predict.py` in the same project folder.

### Windows PowerShell alternative without activation
```
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe predict.py
```

## Understanding results
- **MAE**: average absolute error in marks (smaller is better).
- **R²**: comparison with always predicting the test-set mean (1 is perfect; can be negative).
- Prediction is an estimate, not a guarantee. The script clamps estimates to 0–100.

## Data privacy
Do not include identifiable student information in a public GitHub repository without permission.
