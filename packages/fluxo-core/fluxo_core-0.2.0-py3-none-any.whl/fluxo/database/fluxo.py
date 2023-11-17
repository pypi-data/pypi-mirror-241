import sqlite3
import json
from datetime import datetime
from dataclasses import dataclass
from fluxo.settings import settings_db
from fluxo.utils import utc_current_time_formatted


@dataclass
class Fluxo:
    id: int = None
    name: str = None
    date_of_creation: datetime = None
    interval: dict = None
    active: bool = True

    def save(self):
        date_of_creation = utc_current_time_formatted()
        interval = json.dumps(self.interval)

        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO TB_Fluxo (name, date_of_creation, interval, active)
            VALUES (?, ?, ?, ?)
        ''', (self.name, date_of_creation, interval, self.active))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, name, date_of_creation, interval, active):
        interval = json.dumps(interval)

        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE TB_Fluxo
            SET name=?, date_of_creation=?, interval=?, active=?
            WHERE id=?
        ''', (name, date_of_creation, interval, active, id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TB_Fluxo')
        data = cursor.fetchall()
        conn.close()
        return [Fluxo(*row) for row in data]

    @staticmethod
    def get_by_name(name):
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TB_Fluxo WHERE name=?', (name,))
        data = cursor.fetchone()
        conn.close()
        if data:
            data_list = []
            for value in data:
                data_list.append(value)
            data_list[3] = json.loads(data_list[3])
            return Fluxo(*data_list)
        else:
            return None

    @staticmethod
    def delete(id):
        conn = sqlite3.connect(settings_db.PATH)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM TB_Fluxo WHERE id=?', (id,))
        conn.commit()
        conn.close()

    def __repr__(self) -> str:
        return f'''
            id:                     {self.id},
            name:                   {self.name},
            date_of_creation:       {self.date_of_creation},
            interval:               {self.interval},
            active:                 {self.active},
        '''
