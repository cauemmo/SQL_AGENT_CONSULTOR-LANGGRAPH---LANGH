import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = quote_plus(os.getenv("POSTGRES_PASSWORD"))  # codifica os caracteres especiais!

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(DATABASE_URL)
