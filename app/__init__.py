# app/__init__.py

import os
from flask import Flask
from flask_babel import Babel
from app.routes import bp as main_bp


credentials_path = r'C:\Users\HP\OneDrive - Høgskulen på Vestlandet\Dokumenter\HVL\DAT158\MachineLearning\proj2\credentials.json'
if not os.path.exists(credentials_path):
    print(f"Credentials file not found at: {credentials_path}")
    raise FileNotFoundError(f"Credentials file not found at: {credentials_path}")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path



def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static', 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size: 16MB
              
    babel = Babel(app)
    
    app.register_blueprint(main_bp)
    
    return app
