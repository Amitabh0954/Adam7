import os

class Config:
    DEBUG = os.getenv('FLASK_DEBUG', False)
    TESTING = os.getenv('FLASK_TESTING', False)
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')