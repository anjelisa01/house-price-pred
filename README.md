# 🏠 House Price Prediction

This repository contains a complete machine learning pipeline for predicting house prices based on the classic [Kaggle House Prices dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). The project covers everything from exploratory data analysis (EDA) and feature engineering to model selection, hyperparameter tuning, cross-validation, and deployment.

# What inside?
- old-notebook-houseprice.ipynb : containing full workflow including EDA, feature engineering, hyperparameter tuning and model evaluatin
- notebook_House_Price.ipynb : containinng further improvement of the model to get better accuracy, this version have different approach including doing model selection, revising feature engineering function, use RandomSearch instead GridSearch, and using MLFlow tracking.
- data.json : a json file containing mock input to feed the model.
- feature_engineering.py : module to transform raw input data into suitable format to feed the model.
- app.py : containing FastAPI endpoints
- requirements.txt : all the requirements the app need
- Dockerfile : app docker image

## 🔍 Project Highlights

- ✅ **Extensive EDA**: Thorough exploration of numerical and categorical features.
- 🛠 **Feature Engineering**: Created and transformed features for better predictive power.
- 🤖 **Modeling**: Evaluated multiple models including ensemble and regularized regressors.
- 🔧 **Hyperparameter Tuning**: Grid search with cross-validation for optimal performance.
- 🚀 **Deployment**: Served the trained model locally using FastAPI and Docker.
- ⬆️ **model improvement**: new improved model moves 600 positions up the Kaggle competition leaderboard.

## Notes
The deployment still using the old model, the new improved model is not deployed yet.
