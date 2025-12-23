import streamlit as st
import pandas as pd
import pickle
import os

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Insurance Cost Predictor",
    layout="centered"
)

st.title("💰 Insurance Cost Prediction App")

# ---------------- LOAD MODEL (SAFE WAY) ---------------- #
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "insurance_model.pkl")
    with open(model_path, "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
except Exception as e:
    st.error("❌ Model load nahi ho pa raha. Please check model file or requirements.")
    st.stop()

# ---------------- INPUTS ---------------- #
age = st.number_input("Age", min_value=18, max_value=100, step=1)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=5, step=1)

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

region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0
# Northeast → all zeros

# ---------------- PREDICTION ---------------- #
if st.button("Predict Insurance Cost"):

    input_df = pd.DataFrame([{
        "age": age,
        "children": children,
        "is_female": is_female,
        "is_smoker": is_smoker,
        "bmi_category_obese": bmi_category_obese,
        "region_northwest": region_northwest,
        "region_southeast": region_southeast,
        "region_southwest": region_southwest
    }])

    try:
        prediction = model.predict(input_df)
        st.success(f"💵 Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")
    except Exception as e:
        st.error("❌ Prediction failed. Feature mismatch or model issue.")

































