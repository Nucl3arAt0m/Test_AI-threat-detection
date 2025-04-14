import joblib
import numpy as np

def predict(input_features):
    model = joblib.load('models/threat_model.pkl')
    prediction = model.predict([input_features])
    return 'Attack' if prediction[0] == 1 else 'Normal'
