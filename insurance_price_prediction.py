from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
with open('model_rfr.pkl', 'rb') as file:
    model = pickle.load(file)
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Render the index.html
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        # When JSON data is sent to the server
        data = request.get_json()
    else:
        # When form data is sent to the server
        data = {
            'Age': request.form.get('Age'),
            'Diabetes': request.form.get('Diabetes'),
            'BloodPressureProblems': request.form.get('BloodPressureProblems'),
            'AnyTransplants': request.form.get('AnyTransplants'),
            'AnyChronicDiseases': request.form.get('AnyChronicDiseases'),
            'Height': request.form.get('Height'),
            'Weight': request.form.get('Weight'),
            'KnownAllergies': request.form.get('KnownAllergies'),
            'HistoryOfCancerInFamily': request.form.get('HistoryOfCancerInFamily'),
            'NumberOfMajorSurgeries': request.form.get('NumberOfMajorSurgeries')
        }


    columns = ['Age', 'Diabetes', 'BloodPressureProblems', 'AnyTransplants',
               'AnyChronicDiseases', 'Height', 'Weight', 'KnownAllergies',
               'HistoryOfCancerInFamily', 'NumberOfMajorSurgeries']
    
    df = pd.DataFrame([data], columns=columns)
    scaled_data = scaler.transform(df)
    prediction = model.predict(scaled_data)[0]

    return jsonify({'prediction': round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)