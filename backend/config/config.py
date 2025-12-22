import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default-secret-key")
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "INFO")

config = Config()