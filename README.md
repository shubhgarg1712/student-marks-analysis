Student Performance Analysis & Outlier Detection
Student marks analysis and outlier detection using Python, NumPy and Pandas
# 📊 Student Performance Analysis & Outlier Detection

This project analyzes student marks using **Python, NumPy, and Pandas**.
It calculates statistical measures and detects outliers using the **Z-score method**.

---

## 🚀 Features

* Calculate **mean** and **standard deviation**
* Identify **maximum and minimum marks** with subject mapping
* Detect **outliers using Z-score**
* Display **outlier indices, values, and subjects**
* Clean and structured output

---

## 🛠️ Technologies Used

* Python 🐍
* NumPy
* Pandas

---

## 📌 Concept Used

The project uses the **Z-score method** for outlier detection.

A data point is considered an outlier if:

| Z-score                      | Condition         |
| ---------------------------- | ----------------- |
| |Z| > 1 (for small datasets) | Outlier           |
| |Z| > 2 or 3                 | Standard practice |

---

## ▶️ How to Run

### 1. Install required libraries

```bash
pip install numpy pandas
```

### 2. Run the program

```bash
python outlier_detection.py
```

---

## 📥 Input Example

```
Enter number of subjects: 3
Enter subject name: Math
Enter marks: 60
Enter subject name: Physics
Enter marks: 1000
Enter subject name: English
Enter marks: 50
```

---

## 📤 Output Example

```
--- STATISTICS ---
Marks: [  60 1000   50]
Mean: 370.0
Standard Deviation: 446.0

Maximum marks obtained in Physics is 1000
Minimum marks obtained in English is 50

--- OUTLIERS ---
Outlier indexes: [1]
Outlier marks: [1000]
Outlier subjects: ['Physics']
```

---

## 📊 Project Type

Beginner-level **Data Analysis Project**

---

## 💡 Future Improvements

* Add CSV file input support
* Add data visualization using Matplotlib
* Implement IQR method for better outlier detection

---

## 👨‍💻 Author

**Shubh Garg**
BTech AI Student 
