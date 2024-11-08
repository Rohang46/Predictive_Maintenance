import pandas as pd
import numpy as np
import time

def collect_data():
    # Simulate real-time sensor data
    data = {
        'temperature': np.random.normal(50, 5),
        'vibration': np.random.normal(20, 2),
        'pressure': np.random.normal(100, 10),
        'status': 1  # 1 indicates normal, 0 indicates potential failure
    }
    return data

def save_data():
    while True:
        data = collect_data()
        df = pd.DataFrame([data])
        df.to_csv('data/sensor_data.csv', mode='a', header=False, index=False)
        time.sleep(5)

if __name__ == "__main__":
    save_data()
