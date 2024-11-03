# app/routes.py

import os
from flask import Blueprint, render_template, request, jsonify
from app.utils import classify_image

bp = Blueprint('main', __name__)

upload_folder = os.path.join(os.getcwd(), 'static', 'uploads')
os.makedirs(upload_folder, exist_ok=True)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    class_name, confidence = classify_image(file_path)
    if class_name:
        return jsonify({'class': class_name, 'confidence': round(confidence, 4)})
    else:
        return jsonify({'class': 'No animal detected', 'confidence': 0})
