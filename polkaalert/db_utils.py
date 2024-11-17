import os
import pandas as pd
from sqlalchemy import create_engine, text

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

def create_connection():
    """Cria uma conexão com o banco de dados PostgreSQL usando SQLAlchemy."""
    engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')
    return engine.connect()  # Retorna uma conexão diretamente do engine


def send_query(conn, query, fetchall=False, params=None):
    """Executa uma consulta no banco de dados usando SQLAlchemy."""
    try:
        # Usando SQLAlchemy para executar a consulta
        query = text(query)  # Convertendo a consulta para um objeto executável
        result = conn.execute(query, params)  # Usando execute diretamente no conn
        
        if fetchall:
            print(result.fetchall())
        
        # Não é necessário verificar o conteúdo da consulta. Agora, apenas fazemos commit para INSERT/UPDATE/DELETE
        if query.__str__().strip().lower().startswith(('create', 'drop', 'insert', 'update', 'delete')):
            conn.commit()
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        conn.rollback()  # Rollback em caso de erro

def save_to_database(table_name:str, conn, df:pd.DataFrame, schema:str, if_exists:str) -> None:
    """Salva uma linha de dados no banco de dados usando pandas."""
    df.to_sql(name=table_name,
              con=conn,
              schema=schema, 
              if_exists=if_exists, 
              index=False)  # Salva no banco de dados