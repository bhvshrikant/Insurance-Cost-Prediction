import streamlit as st

# Main header
st.header('Insurance Cost Predictor')

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
