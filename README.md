# 💼 Employee Salary Classification Web App

This project is a Machine Learning-based web application developed using Streamlit. It predicts whether an employee earns more than or less than $50K per year based on multiple input attributes such as age, education, workclass, marital status, occupation, and more. Designed with simplicity and usability in mind, the app provides an interactive interface for users to input data and receive instant prediction

## 🔍 Key points

- **Salary Classification Based on Attributes**  
  Predicts whether an employee earns **more or less than $50K per year** using input attributes like age, education, workclass, marital status, occupation, etc.

- **Interactive Web Interface with Streamlit**  
  Provides a user-friendly interface where users can enter data through sliders, dropdowns, and inputs—no coding required.

- **Machine Learning Model Integration**  
  Uses a trained **Gradient Boosting Regressor** model from Scikit-learn for accurate and fast salary predictions.

- **Real-Time Input Preview**  
  Shows a compact preview of all entered inputs before prediction to ensure transparency and allow verification.

- **Deployment Ready**  
  Easily deployable via **Streamlit Share**, **GitHub**, or any Python-compatible cloud platform.
  
  ---
  
  ### ✅ Features Used

The following attributes were used as input features to train the salary classification model:

- **Age** – Numerical value indicating the age of the individual.
- **Workclass** – Type of employment (e.g., Private, Self-employed, Government).
- **Fnlwgt** – Final weight assigned to the individual by the Census Bureau.
- **Education** – Highest level of education attained.
- **Marital Status** – Marital condition (e.g., Never-married, Divorced).
- **Occupation** – Type of job or role.
- **Relationship** – Relationship status within a household (e.g., Husband, Not-in-family).
- **Race** – Race category (e.g., White, Black, Asian-Pac-Islander).
- **Gender** – Gender of the individual.
- **Capital Gain** – Income from investment sources other than wages.
- **Capital Loss** – Loss from investment or business.
- **Hours per Week** – Number of hours worked per week.
- **Native Country** – Country of origin.

These features help determine whether an individual earns **more than or less than \$50K per year**.


---
### ✅ Model Training Overview

- **Logistic Regression**  
- **Random Forest**  
- **K-Nearest Neighbors (KNN)**  
- **Support Vector Machine (SVM)**  
- **Gradient Boosting Regressor**

The best-performing model (based on accuracy) was saved as `best_model.pkl` using **Joblib** for future use in prediction without retraining.

---

🚀 **Streamlit Web App**  
You can run the Streamlit frontend using the command:  
```bash
streamlit run app.py
