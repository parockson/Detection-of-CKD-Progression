# 🩺 Detection of CKD Progression

A machine learning study that predicts **Chronic Kidney Disease (CKD) stage progression** using clinical and laboratory data, following the **CRISP-DM** framework.

---

## 📌 Overview

Chronic Kidney Disease (CKD) is a silent, progressive condition that often goes undetected until significant kidney damage has occurred. This project leverages machine learning to:

- Predict a patient's **CKD stage** (Stages 0–5) from clinical biomarkers
- Identify the most **influential risk factors** driving progression
- Compare multiple ML algorithms to find the most performant model for clinical use

The dataset is sourced from [Kaggle – CKD Stages Dataset](https://www.kaggle.com/datasets/angad2002/chronic-kidney-disease-ckd-stages-dataset) and contains **400 patient records** with **28 clinical features**.

---

## 📂 Project Structure

```
Detection-of-CKD-Progression/
│
├── Datasets/
│   └── 1/                          # Raw CKD dataset (CSV)
│
├── modelling/
│   ├── notebook.ipynb              # Main analysis & modelling notebook
│   └── model_evaluation_results.csv
│
├── Models/                         # Saved trained model pipelines (.pkl)
│   ├── XGBoost_pipeline.pkl
│   ├── LightGBM_pipeline.pkl
│   ├── Gradient_Boosting_pipeline.pkl
│   ├── Random_Forest_pipeline.pkl
│   ├── ANN_(MLPClassifier)_pipeline.pkl
│   ├── Logistic_Regression_pipeline.pkl
│   └── SVM_pipeline.pkl
│
├── Analysis/                       # Exploratory analysis outputs
├── requirements.txt
└── README.md
```

---

## 🧪 Dataset Features

| Category | Features |
|---|---|
| **Demographics** | Age |
| **Vitals** | Blood Pressure (`bp`) |
| **Urine Tests** | Specific Gravity (`sg`), Albumin (`al`), Sugar (`su`), RBC (`rbc`), Pus Cells (`pc`), Bacteria (`ba`) |
| **Blood Tests** | Blood Glucose (`bgr`), Blood Urea (`bu`), Serum Creatinine (`sc`), Sodium (`sod`), Potassium (`pot`), Hemoglobin (`hemo`), PCV, WBC Count (`wc`), RBC Count (`rc`) |
| **Comorbidities** | Hypertension (`htn`), Diabetes Mellitus (`dm`), Coronary Artery Disease (`cad`) |
| **Symptoms** | Appetite (`appet`), Pedal Edema (`pe`), Anemia (`ane`) |
| **Target** | **GFR** (Glomerular Filtration Rate), **CKD Stage** (0–5) |

> CKD stages are derived from GFR values using the clinically validated **CKD-EPI equation**.

---

## ⚙️ Methodology (CRISP-DM)

1. **Business Understanding** — Define the clinical problem and objectives
2. **Data Understanding** — Explore feature distributions, missing values, and class balance
3. **Data Preparation** — Handle missing values, fix data types, encode categoricals, scale numerics via `Pipeline` + `ColumnTransformer`
4. **Modelling** — Train and tune 7 classifiers
5. **Evaluation** — Compare models on Accuracy, Precision, Recall, F1, ROC-AUC, and Confusion Matrix
6. **Deployment** — Save best-performing pipelines via `joblib`

---

## 📊 Model Results

| Model | Accuracy | F1 Score | ROC AUC |
|---|---|---|---|
| **Gradient Boosting** | **88.5%** | **87.2%** | **97.6%** |
| LightGBM | 86.0% | 84.1% | 97.8% |
| XGBoost | 85.5% | 84.0% | 97.9% |
| Random Forest | 81.5% | 76.5% | 96.8% |
| ANN (MLPClassifier) | 68.0% | 62.8% | 91.7% |
| Logistic Regression | 67.5% | 59.8% | 91.7% |
| SVM | 66.75% | 56.9% | 91.5% |

> 🏆 **Gradient Boosting** achieved the best overall F1 Score and accuracy, making it the recommended model for CKD stage classification.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/parockson/Detection-of-CKD-Progression.git
cd Detection-of-CKD-Progression
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Notebook
Open `modelling/notebook.ipynb` in Jupyter or VS Code and run all cells.

---

## 🔑 Key Libraries

- **Data:** `pandas`, `numpy`
- **Machine Learning:** `scikit-learn`, `xgboost`, `lightgbm`, `catboost`
- **Visualization:** `matplotlib`, `seaborn`, `plotly`
- **Imbalanced Data:** `imbalanced-learn` (SMOTE)
- **Model Persistence:** `joblib`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Dataset by [Angad2002 on Kaggle](https://www.kaggle.com/datasets/angad2002/chronic-kidney-disease-ckd-stages-dataset)
- CKD staging criteria based on [KDIGO Clinical Practice Guidelines](https://kdigo.org/)
