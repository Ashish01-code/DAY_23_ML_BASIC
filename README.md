# DAY_23_ML_BASIC
# Day 23 – Outlier Detection using IQR (Python)

## 📌 Objective
This program analyzes numerical data entered by the user and identifies **outliers** using the **Interquartile Range (IQR) method**, a technique commonly used in **Machine Learning preprocessing** to handle noisy or deviated data points.

---

## 📊 What This Code Does
- Takes user input and stores numbers in a list
- Sorts the dataset
- Calculates:
  - Median
  - First Quartile (Q1)
  - Third Quartile (Q3)
  - Interquartile Range (IQR)
- Determines lower and upper bounds
- Detects and displays outliers

---

## 🧠 Why This Matters in ML
- Outliers can **distort model learning**
- Mean shifts due to extreme values
- IQR is **robust** and works well with skewed data
- Used in:
  - Fraud detection
  - Medical data analysis
  - Sensor data cleaning

---

## 🧮 Key Concepts Used
- Median (robust central tendency)
- Quartiles (Q1, Q3)
- Interquartile Range (IQR = Q3 − Q1)
- Outlier bounds:
  - Lower Bound = Q1 − 1.5 × IQR
  - Upper Bound = Q3 + 1.5 × IQR

---

## 🧪 Sample Flow
1. User enters the number of values
2. Inputs the dataset
3. Program sorts the data
4. Quartiles and IQR are computed
5. Any value outside the bounds is marked as an outlier

---

## 🚀 Learning Outcome
This project builds **ML-ready thinking** by showing:
- Outliers are **deviated signals**, not always errors
- When to keep or remove outliers depends on the problem
- Why preprocessing is critical before training models

---

## 📁 Day
**Day 23 – Statistics for Machine Learning**

---

## 🛠️ Language Used
- Python (Core concepts, no libraries)

---

## ✨ Next Step
Moving forward to **NumPy arrays, vector thinking, and data shapes**, which are fundamental for Machine Learning models.

