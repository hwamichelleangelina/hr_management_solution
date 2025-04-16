!pip install pandas scikit-learn xgboost tensorflow

import joblib
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

from IPython.display import display
from ipywidgets import FileUpload
import io

# load
xgb_model = joblib.load('xgb_model.pkl')
rf_model = joblib.load('rf_model.pkl')
dl_model = load_model('dl_model.h5')
scaler = joblib.load('scaler.pkl')
encoders = joblib.load('label_encoders.pkl')

categorical_cols = list(encoders.keys())
all_columns = [
    'EmployeeId', 'Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'EmployeeCount', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
    'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome',
    'MonthlyRate', 'NumCompaniesWorked', 'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears',
    'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

def input_manual():
    print("\nAnda memilih input manual.")
    print("Silakan masukkan data karyawan sesuai petunjuk yang muncul.\n")

    data = {}
    data['EmployeeId'] = int(input("EmployeeId: "))
    data['Age'] = int(input("Age: "))

    print("BusinessTravel Options: 'Travel_Frequently', 'Travel_Rarely', 'Non-Travel'")
    data['BusinessTravel'] = input("BusinessTravel: ")

    data['DailyRate'] = int(input("DailyRate: "))

    print("Department Options: 'Human Resources', 'Research & Development', 'Sales'")
    data['Department'] = input("Department: ")

    data['DistanceFromHome'] = int(input("DistanceFromHome: "))

    print("Education (1-5)")
    data['Education'] = int(input("Education: "))

    print("EducationField Options: 'Other', 'Medical', 'Life Sciences', 'Marketing', 'Technical Degree', 'Human Resources'")
    data['EducationField'] = input("EducationField: ")

    data['EmployeeCount'] = int(input("EmployeeCount: "))

    print("EnvironmentSatisfaction (1-4)")
    data['EnvironmentSatisfaction'] = int(input("EnvironmentSatisfaction: "))

    print("Gender Options: 'Male', 'Female'")
    data['Gender'] = input("Gender: ")

    data['HourlyRate'] = int(input("HourlyRate: "))

    print("JobInvolvement (1-4)")
    data['JobInvolvement'] = int(input("JobInvolvement: "))

    print("JobLevel (1-5)")
    data['JobLevel'] = int(input("JobLevel: "))

    print("JobRole Options: 'Human Resources', 'Healthcare Representative', 'Research Scientist', 'Sales Executive',\n                  'Manager', 'Laboratory Technician', 'Research Director', 'Manufacturing Director', 'Sales Representative'")
    data['JobRole'] = input("JobRole: ")

    print("JobSatisfaction (1-4)")
    data['JobSatisfaction'] = int(input("JobSatisfaction: "))

    print("MaritalStatus Options: 'Married', 'Single', 'Divorced'")
    data['MaritalStatus'] = input("MaritalStatus: ")

    data['MonthlyIncome'] = int(input("MonthlyIncome: "))
    data['MonthlyRate'] = int(input("MonthlyRate: "))
    data['NumCompaniesWorked'] = int(input("NumCompaniesWorked: "))

    print("Over18: hanya 'Y' yang diperbolehkan")
    data['Over18'] = 'Y'

    print("OverTime Options: 'Yes', 'No'")
    data['OverTime'] = input("OverTime: ")

    data['PercentSalaryHike'] = int(input("PercentSalaryHike: "))

    print("PerformanceRating (1-4)")
    data['PerformanceRating'] = int(input("PerformanceRating: "))

    print("RelationshipSatisfaction (1-4)")
    data['RelationshipSatisfaction'] = int(input("RelationshipSatisfaction: "))

    data['StandardHours'] = int(input("StandardHours: "))

    print("StockOptionLevel (0-3)")
    data['StockOptionLevel'] = int(input("StockOptionLevel: "))

    data['TotalWorkingYears'] = int(input("TotalWorkingYears: "))
    data['TrainingTimesLastYear'] = int(input("TrainingTimesLastYear: "))

    print("WorkLifeBalance (1-4)")
    data['WorkLifeBalance'] = int(input("WorkLifeBalance: "))

    data['YearsAtCompany'] = int(input("YearsAtCompany: "))
    data['YearsInCurrentRole'] = int(input("YearsInCurrentRole: "))
    data['YearsSinceLastPromotion'] = int(input("YearsSinceLastPromotion: "))
    data['YearsWithCurrManager'] = int(input("YearsWithCurrManager: "))

    return pd.DataFrame([data])

def load_from_upload():
    print("Silakan upload file CSV Anda:")
    upload_widget = FileUpload(accept='.csv', multiple=False)
    display(upload_widget)

    while not upload_widget.value:
        pass

    uploaded_file = next(iter(upload_widget.value.values()))
    content = uploaded_file['content']
    df = pd.read_csv(io.BytesIO(content))
    print(f"\nFile '{uploaded_file['metadata']['name']}' berhasil.")
    return df

# choice
print("=== MODE INPUT DATA ===")
print("1. Input manual dari terminal")
print("2. Upload file CSV")
mode = input("Pilih 1 atau 2: ")

if mode == "1":
    df = input_manual()
elif mode == "2":
    df = load_from_upload()
else:
    print("Input tidak valid.")
    exit()

# encode
for col in categorical_cols:
    if col in df.columns:
        df[col] = encoders[col].transform(df[col])

# feature engineering
df['IncomePerYear'] = df['MonthlyIncome'] * 12
df['WorkSatisfaction'] = df['EnvironmentSatisfaction'] + df['JobSatisfaction']
df['RoleSeniorityRatio'] = df['YearsInCurrentRole'] / df['TotalWorkingYears'].replace(0, 1)
df['YearsInCompanyRatio'] = df['YearsAtCompany'] / df['TotalWorkingYears'].replace(0, 1)
df['SeniorityLevel'] = df['JobLevel'] * df['PerformanceRating']
df = df.drop(columns=['MonthlyIncome'])
df = df.drop('EmployeeId', axis=1)
drop_cols = ['MonthlyIncome', 'EmployeeId', 'Attrition', 'EmployeeCount', 'Over18', 'StandardHours']
df_model = df.drop(columns=drop_cols, errors='ignore')

X_new_scaled = scaler.transform(df_model)

# predict
proba_xgb = xgb_model.predict_proba(X_new_scaled)[:, 1]
proba_rf = rf_model.predict_proba(X_new_scaled)[:, 1]
proba_dl = dl_model.predict(X_new_scaled).flatten()

proba_ensemble = (proba_xgb + proba_rf + proba_dl) / 3
pred_ensemble = (proba_ensemble > 0.5).astype(int)

df['Attrition_Prediction'] = pred_ensemble
df['Attrition_Probability'] = proba_ensemble

# hasil akhir
if mode == "2":
    df.to_csv('hasil_prediksi.csv', index=False)
    print("\nPrediksi selesai. Hasil disimpan di 'hasil_prediksi.csv'.")
elif mode == "1":
    print("\n=== DETAIL DATA & PREDIKSI ===")
    print(df.to_string(index=False))
