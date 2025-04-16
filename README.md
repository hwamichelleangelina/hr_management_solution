# Employee Attrition Analysis & Prediction

This project explores the **key factors influencing employee attrition** in a company through **Exploratory Data Analysis (EDA)**, statistical testing, machine learning models, and dashboard visualization.

---

# HR Management System Solution

## Background

**Jaya Jaya Maju** is a multinational company that has been established since the year 2000, employing over 1,000 staff across the country.

Despite its growth, the company continues to face challenges in managing human resources. One critical issue is its **high attrition rate**, which has exceeded **10%** of the total workforce.

To address this, the HR department seeks a **data-driven solution** that can identify the key factors behind employee attrition, enabling the team to take proactive measures and improve employee retention.

## Utilized Tools

- **Jupyter Notebook**: For data processing, EDA, and model development.
- **Looker Studio Dashboard**: [Jaya Jaya Maju Attrition Rate Dashboard for Human Resources Department](https://lookerstudio.google.com/reporting/efed906a-c8f6-4de6-b98c-7eb642ec9705/page/nxCHF)

---

## Project Overview

The primary objective of this project is to **identify and predict** the significant factors that lead to employee attrition, providing insights for the HR department to make informed decisions.

## Steps Taken

### 1. Data Cleaning
- Removed missing values to ensure clean input for analysis and modeling.

### 2. Exploratory Data Analysis (EDA)
- Explored relationships between features and attrition.
- Used visualizations including **correlation heatmaps** to reveal patterns.

### 3. Statistical Testing
- Applied **Chi-Square tests** and **T-tests** to identify statistically significant variables that influence attrition.

### 4. Machine Learning & Deep Learning Models
- Trained and evaluated:
  - **XGBoost**
  - **Random Forest (RF)**
  - **Deep Learning (Neural Network)**
- Achieved an **accuracy of ~85%**.
- Addressed common issues:
  - Used **SMOTE** to handle **imbalanced dataset**.
  - Applied **hyperparameter tuning** to improve generalization and reduce overfitting.

### 5. Dashboard with Looker Studio
- Created a comprehensive dashboard tailored for HR.
- Designed for clarity, integrity, and insight.
- Tracks key factors contributing to employee attrition.

## Key Results

- Successfully identified the most **impactful features** affecting attrition.
- Built **predictive models** with strong performance using balanced and optimized data.
- Delivered a **dashboard** that enables HR to monitor and act on employee trends.

## Tools & Technologies

- **Python**: Pandas, Matplotlib, Seaborn, SciPy, Scikit-learn, XGBoost, TensorFlow/Keras, Imbalanced-learn (SMOTE)
- **Looker Studio**: Interactive and visual HR monitoring dashboard
- **Statistical Analysis**: Chi-Square Test, T-Test
- **Visualization**: Correlation Heatmap, Feature Importance Charts

## Future Improvements

- Integrate **real-time data pipelines** for dynamic dashboard updates.
- Expand model interpretability with tools like **SHAP** or **LIME**.
- Deploy models as APIs for integration with HR systems.
