import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Titanic Survival Prediction")

# Passenger details

pclass = st.selectbox("Passenger Class", [1, 2, 3])

age = st.number_input(
    "Age",
    min_value=0,
    max_value=100,
    value=25
)

sibsp = st.number_input(
    "Number of Siblings/Spouse",
    min_value=0,
    value=0
)

parch = st.number_input(
    "Number of Parents/Children",
    min_value=0,
    value=0
)

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=32.0
)

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

embarked = st.selectbox(
    "Embarked",
    ["C", "Q", "S"]
)

deck = st.selectbox(
    "Deck",
    ["Unknown", "B", "C", "D", "E", "F", "G", "T"]
)


family_size = sibsp + parch + 1

is_alone = 1 if family_size == 1 else 0

sex_male = 1 if sex == "Male" else 0

embarked_q = 1 if embarked == "Q" else 0
embarked_s = 1 if embarked == "S" else 0

deck_b = 1 if deck == "B" else 0
deck_c = 1 if deck == "C" else 0
deck_d = 1 if deck == "D" else 0
deck_e = 1 if deck == "E" else 0
deck_f = 1 if deck == "F" else 0
deck_g = 1 if deck == "G" else 0
deck_t = 1 if deck == "T" else 0
deck_unknown = 1 if deck == "Unknown" else 0

input_data = pd.DataFrame({
    "Pclass": [pclass],
    "Age": [age],
    "SibSp": [sibsp],
    "Parch": [parch],
    "Fare": [fare],
    "Sex_male": [sex_male],
    "Embarked_Q": [embarked_q],
    "Embarked_S": [embarked_s],
    "Deck_B": [deck_b],
    "Deck_C": [deck_c],
    "Deck_D": [deck_d],
    "Deck_E": [deck_e],
    "Deck_F": [deck_f],
    "Deck_G": [deck_g],
    "Deck_T": [deck_t],
    "Deck_Unknown": [deck_unknown],
    "FamilySize": [family_size],
    "IsAlone": [is_alone]
})

if st.button("Predict Survival"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ The passenger is likely to SURVIVE.")
    else:
        st.error("❌ The passenger is NOT likely to survive.")