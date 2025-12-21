import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("insurance_model.pkl", "rb"))

st.set_page_config(page_title="Insurance Cost Predictor", layout="centered")
st.title("💰 Insurance Cost Prediction App")

# Inputs
age = st.number_input("Age", 18, 100, step=1)
bmi = st.number_input("BMI", 10.0, 60.0, step=0.1)
children = st.number_input("Number of Children", 0, 5, step=1)

sex = st.selectbox("Sex", ["Female", "Male"])
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox(
    "Region",
    ["Southwest", "Southeast", "Northwest", "Northeast"]
)

# ---------------- FEATURE ENGINEERING ---------------- #

is_female = 1 if sex == "Female" else 0
is_smoker = 1 if smoker == "Yes" else 0
bmi_category_obese = 1 if bmi >= 30 else 0

# One-hot encoding for region
region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0
# Northeast → all zeros

# ---------------------------------------------------- #

if st.button("Predict Insurance Cost"):

    input_df = pd.DataFrame([{
        'age': age,
        'children': children,
        'is_female': is_female,
        'is_smoker': is_smoker,
        'bmi_category_obese': bmi_category_obese,
        'region_northwest': region_northwest,
        'region_southeast': region_southeast,
        'region_southwest': region_southwest
    }])

    prediction = model.predict(input_df)

    st.success(f"💵 Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")

































