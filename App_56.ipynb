#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
from flask import Flask, request, render_template
import pickle
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model_filename = 'riverwater1_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Load the scaler
scaler_filename = 'scaler1.pkl'
scaler = joblib.load(scaler_filename)

# Define the home route
@app.route('/')
def home():
    return render_template('index1.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the HTML form
        features = [float(request.form[name]) for name in ['ph', 'Hardness', 'Solids', 'Chloroamines', 'Sulfate', 'Conductivity', 'Organic_Carbon', 'Trihalomethanes', 'Turbidity']]
        
        # Transform the features using the scaler
        scaled_features = scaler.transform([features])
        
        # Make predictions using the loaded model
        prediction = model.predict(scaled_features)

        # Determine the output based on the prediction
        if prediction[0] == 1:
            output = "Water is Good you can Drink"
        elif prediction[0] == 0:
            output = "Dont Drink The Water"
        else:
            output = "Not sure"

        # Pass the prediction result to the HTML template
        return render_template('index1.html', prediction_text=output)

    except Exception as e:
        # Handle errors gracefully and provide an appropriate message
        return render_template('index1.html', prediction_text='An error occurred. Please check your input.')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

