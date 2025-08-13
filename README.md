# HDB Flat Resale Price Predictor

**Project Goal:** Predict HDB flat resale prices based on flat features (e.g. flat type, floor area), using machine learning models for supervised regression.

**Programming Language:** Python

 **Models:** Multiple Linear Regression, Decision Tree, XGBoost's Random Forest (Bagging), XGBoost (Boosting), k-Nearest Neighbours (KNN)

**Evaluation Metrics:** R² (R-squared), RMSE (Root Mean Squared Error)

**Best Results:** XGBoost (Boosting), (n_estimators=200, max_depth=10) - R²: 0.9613, RMSE: 35787.8322

**Streamlit App:** [HDB Flat Resale Price Predictor](https://hdb-flat-resale-price-predictor-hr36dfqigzrdvqp2dgxjhg.streamlit.app/)

<img width="3071" height="1537" alt="HDB Flat Resale Price Predictor Streamlit" src="https://github.com/user-attachments/assets/02f51112-2113-48ed-b02b-5966aa936186" />

## Overview

**Data Source:** [data.gov.sg](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view) (Resale flat prices based on registration date from Jan-2017 onwards)

**Key Data Preprocessing:**
- Feature engineering to transform data into a numerical format for quantitative analysis
- Feature selection
- Data splitting into training/validation/test sets
- Numerical feature scaling
- Categorical feature encoding

**Key Evaluation Steps & Insights:**
- Manual hyperparameter tuning for Random Forest and XGBoost:
  - `n_estimators`: number of trees
  - `max_depth`: maximum depth of a tree
- Best-performing models on validation set:
  - Random Forest: `n_estimators`=150, `max_depth`=30
  - XGBoost: `n_estimators`=200, `max_depth`=10
- Interpretation of hyperparameters:
  - Bagging (Random Forest):
    - Trees built independently on random subsets
    - Deep trees (`max_depth`=30) capture complex patterns
    - Moderate number of trees (`n_estimators`=150) sufficient due to averaging
  - Boosting (XGBoost):
    - Trees built sequentially, learning from residual errors
    - Shallower trees (`max_depth`=10) act as weak learners to prevent overfitting
    - More trees (`n_estimators`=200) needed to gradually improve predictions while maintaining generalisation
- Insight: Bagging favours fewer, deeper trees, while boosting prefers more, shallower trees

## Files
- `HDB_Flat_Resale_Price_Predictor.ipynb`: Data preprocessing, model training, tuning, and evaluation
- `ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv`: Raw data (Jan 2017 - May 2025)
- `streamlit_app.py`: Interactive web app for model deployment
- `requirements.txt`: List of dependencies
- `pipeline.pkl`: Saved pipeline for model deployment
- `README.md`: Project overview and instructions

## Local Deployment
### 1. Clone the repository
```
git clone https://github.com/limjiahui3/HDB-Flat-Resale-Price-Predictor.git
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 1. Run the Streamlit app
```
streamlit run streamlit_app.py
