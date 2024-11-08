from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data')
def get_data():
    data = pd.read_csv('data/sensor_data.csv').tail(1)
    return jsonify(data.to_dict(orient="records")[0])

if __name__ == "__main__":
    app.run(debug=True)
