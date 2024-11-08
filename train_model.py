import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def load_data():
    data = pd.read_csv('data/sensor_data.csv')
    X = data[['temperature', 'vibration', 'pressure']]
    y = data['status']
    return X, y

def train_model():
    X, y = load_data()
    model = Sequential([
        Dense(64, activation='relu', input_shape=(X.shape[1],)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=10, batch_size=4)
    model.save('models/predictive_model.h5')
    print("Model training complete and saved.")

if __name__ == "__main__":
    train_model()
