import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# Main header
st.header('Insurance Cost Predictor', divider='grey')

# User's personal details
st.subheader("Personal Information")
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 10, 120, 30)

with col2:
    height = st.slider("Height (cm)", 100, 250, 165)

col1, col2 = st.columns(2)

with col1:
    weight = st.slider("Weight (kg)", 30, 150, 65)

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
    'Diabetes': int(diabetes),
    'BloodPressureProblems': int(blood_pressure),
    'AnyTransplants': int(transplants),
    'AnyChronicDiseases': int(chronic_diseases),
    'Height': height,
    'Weight': weight,
    'KnownAllergies': int(allergies),
    'HistoryOfCancerInFamily': int(cancer_history),
    'NumberOfMajorSurgeries': int(surgeries) if surgeries != "3+" else 3  # Convert 3+ to 3
}

# Create a DataFrame for prediction
input_data = pd.DataFrame([data])


# Load scaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# Load the ML model
with open("model_rfr.pkl", "rb") as file:
    model = pickle.load(file)


# Scale input data
input_data_scaled = scaler.transform(input_data)
input_data_scaled = pd.DataFrame(scaler.transform(input_data), columns=input_data.columns)

# st.write(input_data_scaled)

# Predict the insurance premium
if st.button("Predict Insurance Premium"):
    prediction = model.predict(input_data_scaled)[0]  # Get the first value as the output is an array
    st.write(f"Predicted Insurance Premium: ₹{prediction:.2f}")
