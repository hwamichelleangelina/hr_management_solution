# Attrition Prediction System

This prediction system uses an **ensemble model** to predict the likelihood of employees experiencing attrition (leaving the company). There are two data input methods: **manual** and **uploading a CSV file**.

---

## Models Used

- **XGBoost Model** (`xgb_model.pkl`)
- **Deep Learning Model** (`dl_model.h5`)
- **Random FOrest Model** (`rf_model.h5`)
- The prediction results are the results of **voting ensemble** from all models.

---

## Structure

```
attrition-predictor/
│
├── prediction.py
├── xgb_model.pkl
├── dl_model.h5
├── dl_model.keras
├── rf_model.pkl
├── label_encoders.pkl
├── scaler.pkl
└── README.md
```

---

## How to Run

1. **Prepare Python Environment**

Make sure Python 3.7+ is installed. Then, install dependency:

```bash
pip install pandas scikit-learn xgboost tensorflow
```

2. **Run Script**

In terminal or IDE, run:

```bash
python prediction.py
```

3. **Select Input Mode**

Options will appear:

```
Select input mode:
1. Manual
2. Upload CSV file
```

---

## Mode 1: Manual Input

Fill in employee data one by one via terminal. After all is filled in:

- The model will process the input.

- Prediction is displayed on the screen:
```
=== DATA & PREDICTION DETAILS ===
<Employee data>
Attrition Prediction and Resignation Probability
```

---

## Mode 2: Upload CSV File

1. Prepare a `.csv` file with the appropriate format (input columns such as `EmployeeId`, `Age`, `BusinessTravel`, etc.).
2. Upload when prompted.
3. The system will process the entire row and save the results in:

```
hasil_prediksi.csv
```

This file contains the original data + predicted results for the Attrition column.

---

## Important Notes

- `Over18` is only filled with `'Y'` because all training data is assumed to be 18+.
- Make sure the input format matches the options shown for categorical columns such as:
- `Gender`: `'Male'`, `'Female'`
- `JobRole`: `'Sales Executive'`, `'Research Scientist'`, etc.
- `Education`: Integer from 1 to 5
- Numeric columns must be valid (within a reasonable range).

---
