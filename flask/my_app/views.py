from my_app import app
from flask import request

import sys
sys.path.append(r'./my_app')
from ML import get_prediction


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        return get_prediction(image_bytes=img_bytes)