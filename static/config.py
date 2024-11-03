import os

class Config:
    LANGUAGES = ['en', 'no']
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# ...you can add more configurations as needed
