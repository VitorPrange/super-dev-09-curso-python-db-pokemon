from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from pathlib import Path

RAIZ_PROJEO = Path(__file__).resolve().parent.parent


load_dotenv(RAIZ_PROJEO / ".env")


class Settings ():
    def __init__(self):
        self.db_host: str = os.getenv("DB_HOST")
        self.db_port: int = os.getenv("DB_PORT")
        self.db_user: str = os.getenv("DB_USER")
        self.db_password: str = os.getenv("DB_PASS")
        self.db_name: str = os.getenv("DB_NAME")
        
        self.app_host: str = os.getenv("APP_HOST")
        self.app_port: str = os.getenv("APP_PORT")
        
        
        
settings = Settings()


