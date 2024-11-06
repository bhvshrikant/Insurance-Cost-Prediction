import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Main header
st.header('Insurance Cost Predictor', divider='grey')

# User's personal details
st.subheader("Personal Information")
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 0, 130, 25)

with col2:
    height = st.slider("Height (cm)", 0, 300, 165)

col1, col2 = st.columns(2)

with col1:
    weight = st.slider("Weight (kg)", 0, 200, 65)

# Health-related toggles in a two-column layout
st.subheader("Health Information")
col1, col2 = st.columns(2)

with col1:
    diabetes = st.checkbox("Diabetes")
    blood_pressure = st.checkbox("Blood Pressure Problems")
    allergies = st.checkbox("Known Allergies")
    transplants = st.checkbox("Any Transplants")

with col2:
    chronic_diseases = st.checkbox("Chronic Diseases")
    cancer_history = st.checkbox("Family History of Cancer")
    surgeries = st.selectbox("Major Surgeries", options=["0", "1", "2", "3", "3+"])

# Display selected options
st.write("You selected:")
st.write("- Age:", age)
st.write("- Height:", height)
st.write("- Weight:", weight)
st.write("- Diabetes:", "Yes" if diabetes else "No")
st.write("- Blood Pressure Problems:", "Yes" if blood_pressure else "No")
st.write("- Known Allergies:", "Yes" if allergies else "No")
st.write("- Any Transplants:", "Yes" if transplants else "No")
st.write("- Chronic Diseases:", "Yes" if chronic_diseases else "No")
st.write("- Family History of Cancer:", "Yes" if cancer_history else "No")
st.write("- Number of Major Surgeries:", surgeries)


# Converting categorical inputs to numeric format as per model's requirement
data = {
    'Age': age,
    'Height': height,
    'Weight': weight,
    'Diabetes': int(diabetes),
    'BloodPressureProblems': int(blood_pressure),
    'AnyTransplants': int(transplants),
    'AnyChronicDiseases': int(chronic_diseases),
    'KnownAllergies': int(allergies),
    'HistoryOfCancerInFamily': int(cancer_history),
    'NumberOfMajorSurgeries': int(surgeries) if surgeries != "3+" else 3  # Convert 3+ to 3
}

# Create a DataFrame for prediction
input_data = pd.DataFrame([data])

# Load the ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Predict the insurance premium
if st.button("Predict Insurance Premium"):
    prediction = model.predict(input_data)[0]  # Get the first value in case the output is an array
    st.write(f"Predicted Insurance Premium: ${prediction:.2f}")
