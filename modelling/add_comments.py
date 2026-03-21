import json
import re
import ast

# ─────────────────────────────────────────────
# Comment rules: (regex_pattern, comment_text)
# Applied to individual code lines
# ─────────────────────────────────────────────
COMMENT_RULES = [
    # ── Imports ──────────────────────────────────────────────────────────
    (r"^import pandas",             "Import pandas for DataFrame manipulation"),
    (r"^import numpy",              "Import numpy for numerical operations"),
    (r"^import matplotlib",         "Import matplotlib for static plotting"),
    (r"^import seaborn",            "Import seaborn for statistical visualizations"),
    (r"^import plotly",             "Import plotly for interactive charts"),
    (r"^import joblib",             "Import joblib for saving/loading models"),
    (r"^import warnings",           "Import warnings module"),
    (r"^import scipy",              "Import scipy for statistical functions"),
    (r"^import json",               "Import json for file handling"),
    (r"^import os",                 "Import os for file system operations"),
    (r"^from sklearn\.pipeline",    "Pipeline: chains preprocessing + model into one object"),
    (r"^from sklearn\.preprocessing.*OneHot",  "OneHotEncoder: encode categorical variables"),
    (r"^from sklearn\.preprocessing.*Standard", "StandardScaler: normalise features to mean=0, std=1"),
    (r"^from sklearn\.preprocessing.*MinMax",   "MinMaxScaler: scale features to [0,1] range"),
    (r"^from sklearn\.preprocessing",           "Import preprocessing utilities"),
    (r"^from sklearn\.compose",     "ColumnTransformer: apply different transforms per column type"),
    (r"^from sklearn\.model_selection.*train_test_split", "train_test_split: split data into train/test sets"),
    (r"^from sklearn\.model_selection.*cross_val", "cross_val_score: K-fold cross-validation"),
    (r"^from sklearn\.model_selection",  "Import model selection utilities"),
    (r"^from sklearn\.metrics",     "Import evaluation metrics (accuracy, F1, ROC-AUC, etc.)"),
    (r"^from sklearn\.ensemble.*RandomForest", "RandomForestClassifier: ensemble of decision trees"),
    (r"^from sklearn\.ensemble.*GradientBoosting", "GradientBoostingClassifier: boosted tree ensemble"),
    (r"^from sklearn\.ensemble",    "Import ensemble learning models"),
    (r"^from sklearn\.svm",         "SVC: Support Vector Classifier"),
    (r"^from sklearn\.linear_model.*Logistic", "LogisticRegression: linear probabilistic classifier"),
    (r"^from sklearn\.linear_model", "Import linear model"),
    (r"^from sklearn\.neural_network", "MLPClassifier: multi-layer perceptron (neural network)"),
    (r"^from xgboost",              "XGBoostClassifier: gradient boosted trees (fast & accurate)"),
    (r"^from lightgbm",             "LightGBM: gradient boosted trees optimised for speed"),
    (r"^from catboost",             "CatBoost: gradient boosting with built-in categorical support"),
    (r"^from imblearn",             "SMOTE: synthetic oversampling to fix class imbalance"),
    (r"^from scipy\.stats",         "Import scipy statistical functions"),

    # ── Data Loading ──────────────────────────────────────────────────────
    (r"pd\.read_csv",               "Load dataset from CSV file into a DataFrame"),
    (r"pd\.read_excel",             "Load dataset from Excel file into a DataFrame"),
    (r"\.head\(",                   "Preview the first N rows of the DataFrame"),
    (r"\.tail\(",                   "Preview the last N rows of the DataFrame"),
    (r"\.info\(",                   "Show DataFrame schema: columns, dtypes, and non-null counts"),
    (r"\.describe\(",               "Generate descriptive statistics for numeric columns"),
    (r"\.shape",                    "Return (rows, columns) dimensions of the DataFrame"),
    (r"\.columns",                  "List all column names in the DataFrame"),
    (r"\.dtypes",                   "Show data type of each column"),
    (r"\.nunique\(",                "Count unique values in each column"),
    (r"\.unique\(",                 "Return array of unique values in the column"),
    (r"\.value_counts\(",           "Count occurrences of each unique value"),
    (r"\.sample\(",                 "Randomly sample N rows from the DataFrame"),

    # ── Missing Values ────────────────────────────────────────────────────
    (r"\.isnull\(\)\.sum\(",        "Count missing values per column"),
    (r"\.isnull\(\)",               "Boolean mask: True where value is NaN"),
    (r"\.isna\(\)",                 "Boolean mask: True where value is NaN"),
    (r"\.notnull\(",                "Boolean mask: True where value is NOT NaN"),
    (r"\.dropna\(",                 "Drop rows (or columns) that contain NaN values"),
    (r"\.fillna\(",                 "Fill missing values with the specified value or strategy"),
    (r"SimpleImputer|\.fit_transform\(.*imputer", "Impute missing values using the chosen strategy"),
    (r"\.notna\(",                  "Filter to rows where the column value is not NaN"),

    # ── Data Cleaning / Type Conversion ──────────────────────────────────
    (r"\.astype\(",                 "Cast column to the specified data type"),
    (r"pd\.to_numeric",             "Convert column to numeric, coercing errors to NaN"),
    (r"\.replace\(",                "Replace specific values in the Series/DataFrame"),
    (r"\.strip\(",                  "Remove leading/trailing whitespace from string values"),
    (r"\.lower\(",                  "Convert string values to lowercase"),
    (r"\.upper\(",                  "Convert string values to uppercase"),
    (r"\.rename\(",                 "Rename columns or index labels"),
    (r"\.drop\(",                   "Remove specified rows or columns"),
    (r"\.reset_index\(",            "Reset the DataFrame index to default integer index"),
    (r"\.copy\(",                   "Create an independent copy of the DataFrame"),

    # ── Exploratory Data Analysis ─────────────────────────────────────────
    (r"\.corr\(",                   "Compute pairwise correlation between numeric columns"),
    (r"sns\.heatmap",               "Plot correlation heatmap using seaborn"),
    (r"sns\.countplot",             "Bar chart of category frequencies"),
    (r"sns\.boxplot",               "Box plot to visualise distribution and outliers"),
    (r"sns\.histplot|sns\.distplot","Distribution/histogram plot of the variable"),
    (r"sns\.barplot",               "Bar chart showing means with confidence intervals"),
    (r"sns\.violinplot",            "Violin plot combining box plot and KDE"),
    (r"sns\.pairplot",              "Scatter matrix for pairwise feature relationships"),
    (r"sns\.scatterplot",           "Scatter plot for two numeric variables"),
    (r"plt\.figure\(",              "Create a new matplotlib figure with specified size"),
    (r"plt\.title\(",               "Set the chart title"),
    (r"plt\.xlabel\(",              "Label for the x-axis"),
    (r"plt\.ylabel\(",              "Label for the y-axis"),
    (r"plt\.xticks\(",              "Customise x-axis tick labels"),
    (r"plt\.yticks\(",              "Customise y-axis tick labels"),
    (r"plt\.legend\(",              "Add legend to the plot"),
    (r"plt\.tight_layout\(",        "Automatically adjust subplot spacing"),
    (r"plt\.show\(",                "Render and display the chart"),
    (r"plt\.savefig\(",             "Save the figure to a file"),
    (r"plt\.subplot\(",             "Create a subplot at the given grid position"),
    (r"plt\.subplots\(",            "Create a figure with a grid of subplots"),
    (r"px\.",                       "Create an interactive Plotly chart"),

    # ── Feature Engineering ───────────────────────────────────────────────
    (r"LabelEncoder|\.fit_transform\(.*encoder", "Encode labels as integers"),
    (r"OneHotEncoder|pd\.get_dummies", "One-hot encode categorical column(s)"),
    (r"StandardScaler|MinMaxScaler",   "Scale numeric features for model compatibility"),
    (r"ColumnTransformer\(",           "Apply different transformations to different column sets"),
    (r"SelectKBest|RFE|feature_import","Select or rank features by importance"),

    # ── Class Imbalance ───────────────────────────────────────────────────
    (r"SMOTE\(",                    "Initialise SMOTE oversampler to balance class distribution"),
    (r"\.fit_resample\(",           "Resample training data to balance class counts using SMOTE"),

    # ── Train/Test Split ──────────────────────────────────────────────────
    (r"train_test_split\(",         "Split data into training and test sets (stratified by class)"),
    (r"\bX_train\b.*=",            "Feature matrix for training"),
    (r"\bX_test\b.*=",             "Feature matrix for evaluation (unseen during training)"),
    (r"\by_train\b.*=",            "Target labels for training"),
    (r"\by_test\b.*=",             "True labels for the test set"),

    # ── Model Definition / Pipeline ───────────────────────────────────────
    (r"Pipeline\(\[",              "Build a pipeline: preprocessing → model in one object"),
    (r"RandomForestClassifier\(",  "Random Forest: ensemble of decision trees via bagging"),
    (r"GradientBoostingClassifier\(", "Gradient Boosting: sequential boosted tree ensemble"),
    (r"XGBClassifier\(",           "XGBoost classifier with regularisation"),
    (r"LGBMClassifier\(",          "LightGBM: leaf-wise grown boosted trees"),
    (r"CatBoostClassifier\(",      "CatBoost: boosted trees with native categorical support"),
    (r"LogisticRegression\(",      "Logistic Regression: linear probabilistic classifier"),
    (r"SVC\(",                     "Support Vector Classifier with kernel trick"),
    (r"MLPClassifier\(",           "Artificial Neural Network (multi-layer perceptron)"),

    # ── Model Training ────────────────────────────────────────────────────
    (r"\.fit\(X_train",            "Train the model on the training data"),
    (r"\.fit\(",                   "Fit the model/transformer to the data"),

    # ── Predictions ───────────────────────────────────────────────────────
    (r"\.predict\(X_test",         "Generate class predictions on the test set"),
    (r"\.predict_proba\(X_test",   "Generate class probability scores on the test set"),
    (r"\.predict\(",               "Generate predictions from the trained model"),

    # ── Evaluation ───────────────────────────────────────────────────────
    (r"accuracy_score\(",          "Calculate proportion of correctly classified samples"),
    (r"precision_score\(",         "Precision: TP / (TP + FP) per class"),
    (r"recall_score\(",            "Recall (sensitivity): TP / (TP + FN) per class"),
    (r"f1_score\(",                "F1: harmonic mean of precision and recall"),
    (r"roc_auc_score\(",           "ROC-AUC: model's ability to distinguish classes"),
    (r"confusion_matrix\(",        "Confusion matrix: actual vs predicted class counts"),
    (r"classification_report\(",   "Full per-class precision, recall, F1 report"),
    (r"cross_val_score\(",         "K-fold cross-validation scores for robust evaluation"),
    (r"ConfusionMatrixDisplay",    "Plot the confusion matrix as a labelled heatmap"),

    # ── Model Saving / Loading ────────────────────────────────────────────
    (r"joblib\.dump\(",            "Serialize and save the trained pipeline to disk"),
    (r"joblib\.load\(",            "Load a previously saved model pipeline from disk"),

    # ── Miscellaneous ─────────────────────────────────────────────────────
    (r"warnings\.filterwarnings",  "Suppress non-critical warnings for cleaner output"),
    (r"np\.where\(",               "Vectorised conditional: if condition, value_a, else value_b"),
    (r"np\.log\(",                 "Natural log transformation (reduces skew)"),
    (r"np\.sqrt\(",                "Square root transformation"),
    (r"np\.isnan\(",               "Boolean check for NaN values using numpy"),
    (r"pd\.DataFrame\(",           "Construct a new DataFrame"),
    (r"pd\.Series\(",              "Construct a new Series"),
    (r"pd\.concat\(",              "Concatenate DataFrames along rows or columns"),
    (r"pd\.merge\(",               "Merge/join two DataFrames on a key column"),
    (r"\.groupby\(",               "Group rows by a column for aggregation"),
    (r"\.agg\(",                   "Apply aggregation function(s) to grouped data"),
    (r"\.sort_values\(",           "Sort DataFrame rows by one or more columns"),
    (r"\.apply\(",                 "Apply a function element-wise or row/column-wise"),
    (r"\.map\(",                   "Map values using a dictionary or function"),
    (r"print\(",                   "Print output to the console"),
    (r"display\(",                 "Render rich output (tables, plots) in the notebook"),
    (r"\.set_index\(",             "Set the specified column as the DataFrame index"),
    (r"\.loc\[",                   "Label-based row/column selection"),
    (r"\.iloc\[",                  "Integer-position-based row/column selection"),
]

# ─────────────────────────────────────────────
# Helper: assign a comment to a single line
# ─────────────────────────────────────────────
def get_comment(line):
    stripped = line.strip()
    # Skip blank lines, existing comments, docstrings, magic commands
    if not stripped or stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
        return None
    if stripped.startswith('%') or stripped.startswith('!'):
        return None
    for pattern, comment in COMMENT_RULES:
        if re.search(pattern, stripped):
            return comment
    return None


def add_comments_to_source(source_lines):
    """
    Takes the list of source strings from a notebook cell (each ending with \n)
    and returns a new list with inline comments appended where appropriate.
    """
    result = []
    for raw_line in source_lines:
        # Each element may or may not end with \n
        line_body = raw_line.rstrip('\n')
        newline   = '\n' if raw_line.endswith('\n') else ''

        # Already has a comment on this line?
        # (simplistic check – splits on # outside strings)
        stripped = line_body.strip()
        if stripped.startswith('#') or not stripped:
            result.append(raw_line)
            continue

        comment = get_comment(line_body)
        if comment:
            # Avoid duplicating comments that are already there
            if '#' in line_body:
                result.append(raw_line)
            else:
                result.append(f"{line_body}  # {comment}{newline}")
        else:
            result.append(raw_line)
    return result


# ─────────────────────────────────────────────
# Main: process notebook
# ─────────────────────────────────────────────
with open('notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

modified = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and cell['source']:
        new_source = add_comments_to_source(cell['source'])
        if new_source != cell['source']:
            cell['source'] = new_source
            modified += 1

print(f"Added comments to {modified} code cells.")

with open('notebook.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Notebook saved successfully.")
