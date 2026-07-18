#  Titanic Survival Prediction using Machine Learning

A Machine Learning web application that predicts whether a passenger would survive the Titanic disaster based on passenger information. The project includes data preprocessing, feature engineering, model training using Gradient Boosting, and deployment through Streamlit.

---

##  Project Overview

The Titanic Survival Prediction project demonstrates an end-to-end Machine Learning workflow, starting from data preprocessing and feature engineering to model training and deployment.

The application accepts passenger details through an interactive web interface and predicts survival using a trained **Gradient Boosting Classifier**.

---

## Live Demo

🔗 **Streamlit App:** *(https://titanic-survival-prediction-cb3ro9gpjhffoaud5v4fzc.streamlit.app/)*

---

##  Dataset

- **Dataset:** Titanic Dataset
- **Source:** Kaggle
- Contains passenger details such as:
  - Passenger Class
  - Age
  - Gender
  - Fare
  - Embarkation Port
  - Cabin Deck
  - Number of Siblings/Spouses
  - Number of Parents/Children

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

##  Machine Learning Pipeline

### Data Preprocessing

- Missing value handling
- Categorical encoding
- Feature engineering
- Dataset cleaning

### Feature Engineering

The following additional features were created:

- Family Size
- Is Alone
- Cabin Deck Encoding
- One-Hot Encoding for categorical variables

---

##  Model Used

**Gradient Boosting Classifier**

Reasons for choosing this model:

- Better generalization than a single Decision Tree
- Handles non-linear relationships effectively
- High predictive performance on structured/tabular datasets
- Less prone to overfitting

---

##  Features Used

- Passenger Class
- Age
- Fare
- Number of Siblings/Spouses
- Number of Parents/Children
- Gender
- Embarked Port
- Cabin Deck
- Family Size
- Is Alone

---

##  Web Application

The Streamlit application allows users to:

- Enter passenger details
- Generate real-time survival predictions
- Use a simple and interactive interface
- Make predictions instantly using the trained model

---

##  Project Structure

```
Titanic_Survival_Prediction/
│
├── Data/
├── Notebooks/
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Titanic-Survival-Prediction.git
```

Move into the project directory

```bash
cd Titanic-Survival-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

##  Application Preview

<img width="1387" height="821" alt="image" src="https://github.com/user-attachments/assets/9057f8f7-fa8e-4c1f-a98d-5131f83ecc58" />
<img width="1150" height="210" alt="image" src="https://github.com/user-attachments/assets/4d8bcc0a-9461-43ff-94cf-bb52609d9b54" />




##  Future Improvements

- Hyperparameter tuning
- Model comparison with XGBoost and LightGBM
- Explainable AI using SHAP
- Docker deployment
- CI/CD pipeline
- User authentication and prediction history

---



## ⭐ If you found this project useful, consider giving it a Star!
