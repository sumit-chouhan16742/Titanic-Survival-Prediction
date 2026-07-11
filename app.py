import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

with open("titanic_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🚢 Titanic Survival Predictor")

st.markdown("""
Curious whether a passenger would have survived the Titanic disaster?

Fill in the passenger details below and click **Predict Survival**.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    age = st.slider("Age", 0, 80, 25)
    sibsp = st.number_input("Siblings / Spouses Aboard", 0, 10, 0)

with col2:
    fare = st.number_input("Fare", min_value=0.0, value=32.0)
    parch = st.number_input("Parents / Children Aboard", 0, 10, 0)
    sex = st.selectbox("Gender", ["Male", "Female"])

st.subheader("Additional Details")

col3, col4 = st.columns(2)

with col3:
    embarked = st.selectbox("Embarked", ["C", "Q", "S"])
    alone = st.selectbox("Travelling Alone?", ["Yes", "No"])

with col4:
    adult_male = st.selectbox("Adult Male?", ["Yes", "No"])
    who = st.selectbox("Passenger Type", ["Man", "Woman", "Child"])

# Encoding
sex = 1 if sex == "Male" else 0
adult_male = 1 if adult_male == "Yes" else 0
alone = 1 if alone == "Yes" else 0

embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

who_man = 1 if who == "Man" else 0
who_woman = 1 if who == "Woman" else 0

if st.button("Predict Survival"):

    input_data = pd.DataFrame({
        "pclass": [pclass],
        "sex": [sex],
        "age": [age],
        "sibsp": [sibsp],
        "parch": [parch],
        "fare": [fare],
        "adult_male": [adult_male],
        "alone": [alone],
        "embarked_Q": [embarked_Q],
        "embarked_S": [embarked_S],
        "who_man": [who_man],
        "who_woman": [who_woman]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.divider()

    if prediction == 1:
        st.success("🎉 The passenger is likely to survive.")
        st.metric("Survival Probability", f"{probability[1]*100:.2f}%")
    else:
        st.error("❌ The passenger is unlikely to survive.")
        st.metric("Survival Probability", f"{probability[0]*100:.2f}%")
