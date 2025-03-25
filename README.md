# Chronic Kidney Disease (CKD) Progression Prediction

## 📌 Project Overview
This project aims to predict the **progression of Chronic Kidney Disease (CKD)** using **machine learning models**. It integrates **clinical data** and applies **multiple classification algorithms** to predict CKD stages, helping in early intervention and treatment planning.

## 📂 Dataset Information
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/857/risk+factor+prediction+of+chronic+kidney+disease)
- **Number of Instances:** 400
- **Number of Features:** 28 (clinical and demographic data)
- **Target Variable:** `ckd_stage` (CKD progression stage from 1 to 5)
- **Feature Categories:**
  - **Numerical:** Age, Blood Pressure (bp), Blood Glucose (bgr), Serum Creatinine (sc), Hemoglobin (hemo), etc.
  - **Categorical:** Hypertension (htn), Diabetes Mellitus (dm), Coronary Artery Disease (cad), Anemia (ane), etc.

## 📊 Methodology
We use the **CRISP-DM Framework** (Cross-Industry Standard Process for Data Mining):
1. **Business Understanding** - Define the research objectives.
2. **Data Understanding** - Exploratory Data Analysis (EDA) to assess data quality.
3. **Data Preparation** - Handling missing values, outliers, and feature transformations.
4. **Modeling** - Train multiple ML models.
5. **Evaluation** - Compare models using performance metrics.
6. **Deployment** - Save trained models for future use.

## 🔧 Preprocessing Pipeline
The preprocessing pipeline includes:
- **Handling Missing Values:** Mean imputation (numerical) and mode imputation (categorical).
- **Feature Engineering:** Encoding categorical variables using **One-Hot Encoding**.
- **Feature Scaling:** Standardizing numerical features with **StandardScaler**.
- **Feature Selection:** Removing highly correlated and clinically irrelevant features.

## 🚀 Machine Learning Models Used
We implemented and compared the following models:
1. **Random Forest Classifier**
2. **XGBoost Classifier**
3. **LightGBM Classifier**
4. **Support Vector Machine (SVM)**
5. **Logistic Regression**

## 📈 Model Evaluation Metrics
We evaluated models based on:
- **Accuracy** - Overall correctness of predictions.
- **Precision** - How many predicted positives were correct.
- **Recall (Sensitivity)** - Ability to identify actual positives.
- **F1 Score** - Balance between Precision and Recall.
- **AUC-ROC Score** - Ability to distinguish between classes.
- **Confusion Matrix** - Breakdown of actual vs. predicted classifications.

## 🔥 Results Summary
| Model                | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|----------------------|----------|-----------|--------|----------|---------|
| Random Forest       | 97.50%   | 98.06%    | 97.50% | 97.59%   | 99.26   |
| XGBoost            | 96.25%   | 97.38%    | 96.25% | 96.49%   | 99.78   |
| LightGBM           | 96.25%   | 96.90%    | 96.25% | 96.33%   | 99.95   |
| SVM                | 72.50%   | 70.54%    | 72.50% | 70.25%   | 94.92   |
| Logistic Regression| 83.75%   | 83.58%    | 83.75% | 83.13%   | 96.61   |

## 🛠 How to Run the Project
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the Preprocessing Pipeline**
```python
python preprocessing.py
```

### **3️⃣ Train Models**
```python
python train_models.py
```

### **4️⃣ Evaluate Models**
```python
python evaluate_models.py
```

## 📌 Future Improvements
- **Hyperparameter tuning** to improve model performance.
- **Integration with a web app** for real-time predictions.
- **Using deep learning models** for enhanced accuracy.

## 📜 License
This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

## 🤝 Acknowledgments
- **Eric Osei Opoku (PHD)** for guidance and supervison.
- **Azubi Africa for training in ML** for the dataset.
- **UCI Machine Learning Repository** for the dataset.
- **Scikit-Learn, XGBoost, LightGBM** for machine learning models.
- **Matplotlib & Seaborn** for data visualization.

---
🔥 **Developed by:** Prince Rockson for an MSc Health Informatics Thesis  
📧 **Contact:** parockson@gmail.com or parockson@st.knust.edu.gh  

