from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('accident_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    speed = int(request.form['speed'])
    weather = int(request.form['weather'])
    traffic = int(request.form['traffic'])

    prediction = model.predict([[speed, weather, traffic]])

    levels = {
        0: "Low Severity",
        1: "Medium Severity",
        2: "High Severity"
    }

    result = levels[prediction[0]]

    return render_template('index.html',
                           prediction_text=f'Predicted Severity: {result}')

if __name__ == '__main__':
    app.run(debug=True)