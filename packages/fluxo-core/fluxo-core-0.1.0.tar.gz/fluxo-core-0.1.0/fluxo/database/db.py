import os
import sqlite3
from fluxo.settings import settings_db


def _verify_if_db_exists(path_db: str = settings_db.PATH):
    if not os.path.exists(path_db):
        create_db(path_db)


def create_db(path_db: str):
    # Conexão com o banco de dados
    conn = sqlite3.connect(path_db)

    # Criar tabela TB_Fluxo
    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS TB_Fluxo (
                id INTEGER PRIMARY KEY,
                name TEXT,
                date_of_creation DATE,
                interval TEXT,
                active BOOLEAN
            )
        ''')
        print('++ tabela TB_Fluxo criada com sucesso')
    except Exception as err:
        print(f'++ Erro ao criar a tabela TB_Fluxo: {err}')

    # Criar tabela TB_Task
    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS TB_Task (
                id INTEGER PRIMARY KEY,
                name TEXT,
                execution_date DATE,
                fluxo_id INTEGER,
                start_time DATE,
                end_time DATE,
                error TEXT,
                FOREIGN KEY (fluxo_id) REFERENCES TB_Fluxo(id) ON DELETE CASCADE
            )
        ''')
        print('++ tabela TB_Task criada com sucesso')
    except Exception as err:
        print(f'++ Erro ao criar a tabela TB_Task: {err}')
    finally:
        # Confirmar as alterações
        conn.commit()
        # Fechando a conexão com o banco de dados
        conn.close()
