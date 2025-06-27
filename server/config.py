import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    CORS_SUPPORTS_CREDENTIALS = True
    CORS_ORIGINS = [
        "http://localhost:5173",
        "http://localhost:5175",
        "https://https-github-com-olella93-frontend.onrender.com"
    ]

    RATELIMIT_STORAGE_URI = "memory://"  

    #JWT Expiration settings
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
