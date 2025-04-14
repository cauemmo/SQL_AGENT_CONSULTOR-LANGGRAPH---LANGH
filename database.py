import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Lê os dados do banco do .env
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

# Cria a string de conexão
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"

# Cria o engine para se conectar ao banco
engine = create_engine(DATABASE_URL)
