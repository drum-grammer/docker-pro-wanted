import json
from typing import Optional
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = Path(__file__).resolve().parent.parent #/db
json_path = str(BASE_DIR/"secrets.json")

def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),  # /app/secrets.json
):
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")

DB_ID = get_secret("DB_ID")
DB_PWD = get_secret("DB_PWD")
DB_URL = get_secret("DB_URL")
DB_PORT = get_secret("DB_PORT")

# SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
SQLALCHEMY_DATABASE_URL =f"mysql+pymysql://{DB_ID}:{DB_PWD}@{DB_URL}:{DB_PORT}/app"

# SQLite Only
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False})

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()