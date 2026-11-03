#Step 1 -Import libraries
"""Predict a student's current mark using the saved model."""
from pathlib import Path
import joblib

#Step 2 - Locate and Check the model

MODEL_FILE = Path(__file__).resolve().parent / "models" / "student_model.pkl"

if not MODEL_FILE.exists():
    print("Model not found. Run all cells in train_model.ipynb first.")
    raise SystemExit(1)

#Step 3 - Load the trained model

model = joblib.load(MODEL_FILE)  # Load only model files you created or trust.

#Step 4- Validate user input

def ask_number(message):
    while True:
        try:
            value = float(input(message))
            if 0 <= value <= 100:
                return value
            print("Please enter a number from 0 to 100.")
        except ValueError:
            print("Please enter a valid number.")


attendance = ask_number("Attendance percentage (0-100): ")
previous = ask_number("Previous mark (0-100): ")
assignment = ask_number("Assignment mark (0-100): ")

#Step 5 - Prepare Student data

# Use a DataFrame so feature names match those used for training.
import pandas as pd
new_student = pd.DataFrame([{
    "attendance": attendance,
    "previous_mark": previous,
    "assignment_mark": assignment,
}])

#Step 6 - Predict and Display the Result

prediction = float(model.predict(new_student)[0])
prediction = max(0, min(100, prediction))
print(f"Estimated current mark: {prediction:.1f}/100")
