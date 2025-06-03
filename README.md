# HDB Flat Resale Price Predictor

**Project Goal:** Predict HDB flat resale prices based on flat features (e.g. flat type, floor area), using machine learning models for supervised regression.

## Overview

 **Models:** Multiple Linear Regression, Decision Tree, XGBoost's Random Forest (Bagging), XGBoost (Boosting), k-Nearest Neighbours (KNN)

**Evaluation Metrics:** R² (R-squared), RMSE (Root Mean Squared Error)

**Best Results:** XGBoost (Boosting), (n_estimators=200, max_depth=10) - R²: 0.9613, RMSE: 35787.8322

**Streamlit App:** [HDB Flat Resale Price Predictor](https://hdb-flat-resale-price-predictor-hr36dfqigzrdvqp2dgxjhg.streamlit.app/)


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
