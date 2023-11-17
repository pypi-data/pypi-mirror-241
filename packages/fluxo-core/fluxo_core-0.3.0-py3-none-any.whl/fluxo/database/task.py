import sqlite3
from datetime import datetime
from dataclasses import dataclass
from fluxo.settings import settings_db
from fluxo.utils import current_time_formatted


@dataclass
class Task:
    id: int = None
    name: str = None
    execution_date: datetime = None
    fluxo_id: int = None
    start_time: datetime = None
    end_time: datetime = None
    error: str = None

    def save(self):

        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO TB_Task (name, execution_date, fluxo_id, start_time, end_time, error)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.name, self.execution_date, self.fluxo_id, self.start_time, self.end_time, self.error))
        conn.commit()

        # Recuperar o ID da tarefa após a inserção
        cursor.execute('SELECT last_insert_rowid()')
        task_id = cursor.fetchone()[0]

        conn.close()

        return Task.get_by_id(task_id)

    @staticmethod
    def update(id, name, execution_date, fluxo_id, start_time, end_time, error):
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE TB_Task
            SET name=?, execution_date=?, fluxo_id=?, start_time=?, end_time=?, error=?
            WHERE id=?
        ''', (name, execution_date, fluxo_id, start_time, end_time, error, id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TB_Task')
        data = cursor.fetchall()
        conn.close()
        if data:
            return [Task(*row) for row in data]
        else:
            return None

    @staticmethod
    def get_by_name(name):
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TB_Task WHERE name=?', (name,))
        data = cursor.fetchone()
        conn.close()
        if data:
            return Task(*data)
        else:
            return None

    @staticmethod
    def get_by_id(id):
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TB_Task WHERE id=?', (id,))
        data = cursor.fetchone()
        conn.close()
        if data:
            return Task(*data)
        else:
            return None

    @staticmethod
    def get_all_by_fluxo_id(fluxo_id):
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TB_Task WHERE fluxo_id=?', (fluxo_id,))
        data = cursor.fetchall()
        conn.close()
        if data:
            return [Task(*row) for row in data]
        else:
            return None

    @staticmethod
    def delete(id):
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM TB_Task WHERE id=?', (id,))
        conn.commit()
        conn.close()

    def __repr__(self) -> str:
        return f'''
            id:                     {self.id},
            name:                   {self.name},
            execution_date:         {self.execution_date},
            fluxo_id:               {self.fluxo_id},
            start_time:             {self.start_time},
            end_time:               {self.end_time},
            error:                  {self.error},
        '''
