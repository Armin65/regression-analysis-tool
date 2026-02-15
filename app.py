from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded."}), 400
    data = pd.read_csv(file)
    return jsonify({"message": "File uploaded successfully", "data": data.to_dict()}), 200

@app.route('/train', methods=['POST'])
def train_model():
    json_data = request.get_json()
    X = np.array(json_data['X']).reshape(-1, 1)
    y = np.array(json_data['y'])
    model = LinearRegression()
    model.fit(X, y)
    return jsonify({"message": "Model trained successfully", "coefficients": model.coef_.tolist(), "intercept": model.intercept_.tolist()}), 200

@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json()
    X_new = np.array(json_data['X']).reshape(-1, 1)
    predictions = model.predict(X_new)
    return jsonify({"predictions": predictions.tolist()}), 200

if __name__ == '__main__':
    app.run(debug=True)
