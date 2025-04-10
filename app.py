import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_file = "insurance.pkl"
model = joblib.load(model_file)

# Input ranges and options
age_range = (0, 100)
bmi_range = (10, 60)
bp_range = (60, 150)
children_range = (0, 10)

gender_options = ['Male', 'Female']
diabetic_options = ['No', 'Yes']
smoker_options = ['No', 'Yes']
region_options = ['Southeast', 'Northwest', 'Southwest', 'Northeast']

def get_user_inputs():
    st.sidebar.header("User Input")
    age = st.sidebar.slider("Age", *age_range, value=30)
    gender = st.sidebar.selectbox("Gender", gender_options)
    bmi = st.sidebar.slider("BMI", *bmi_range, value=25)
    blood_pressure = st.sidebar.slider("Blood Pressure", *bp_range, value=80)
    diabetic = st.sidebar.selectbox("Diabetic", diabetic_options)
    children = st.sidebar.slider("Children", *children_range, value=0)
    smoker = st.sidebar.selectbox("Smoker", smoker_options)
    region = st.sidebar.selectbox("Region", region_options)
    return age, gender, bmi, blood_pressure, diabetic, children, smoker, region

def predict_claim(age, gender, bmi, blood_pressure, diabetic, children, smoker, region):
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender.lower()],
        'bmi': [bmi],
        'bloodpressure': [blood_pressure],
        'diabetic': [diabetic],
        'children': [children],
        'smoker': [smoker],
        'region': [region.lower()]
    })
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Insurance Claim Estimator")
    age, gender, bmi, blood_pressure, diabetic, children, smoker, region = get_user_inputs()
    if st.sidebar.button("Predict"):
        prediction = predict_claim(age, gender, bmi, blood_pressure, diabetic, children, smoker, region)
        st.subheader("Estimated Claim Amount:")
        st.write(f"${prediction:,.2f}")

if __name__ == "__main__":
    main()
