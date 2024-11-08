import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import time

def load_data():
    return pd.read_csv('data/sensor_data.csv').tail(1)

def monitor():
    model = load_model('models/predictive_model.h5')
    print("Monitoring for potential failures...")
    
    while True:
        data = load_data()
        X = data[['temperature', 'vibration', 'pressure']]
        prediction = model.predict(X)
        if prediction[0] > 0.5:  # Assume >0.5 probability indicates a potential failure
            print("Alert: Potential failure detected. Take action!")
        else:
            print("System operating normally.")
        time.sleep(10)

if __name__ == "__main__":
    monitor()
