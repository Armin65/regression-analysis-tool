from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load data
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    data = pd.read_csv(file)
    return jsonify({'message': 'File uploaded successfully', 'data_head': data.head().to_dict()})

# Analyze data
@app.route('/analyze', methods=['POST'])
def analyze_data():
    data = request.get_json()
    X = data['X']  # Assuming that 'X' is provided in the request
    y = data['y']  # Assuming that 'y' is provided in the request
    coefficients = np.polyfit(X, y, 1)  # Simple linear regression
    return jsonify({'coefficients': coefficients.tolist()})

# Endpoint for visualizing results
@app.route('/visualize', methods=['GET'])
def visualize_results():
    # Visualization logic here (e.g., using matplotlib or seaborn)
    return jsonify({'message': 'Visualization not implemented'})

if __name__ == '__main__':
    app.run(debug=True)