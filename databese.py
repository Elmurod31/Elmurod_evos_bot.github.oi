import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("evos.db")
        self.cursor = self.conn.cursor()
    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        first_name varchar(55) not null,
        last_name varchar(55),
        age integer,
        address varchar(255),
        telegram_id integer not null unique, 
        lang varchar(55) default 'uz')
        """)
    def get_user(self, telegram_id):
        user = self.cursor.execute("""
        select * from users where telegram_id = ?
        """, (telegram_id,)).fetchone()
        return user if user else None

    def insert_user(self, first_name, last_name, telegram_id):
        self.cursor.execute("""
        insert into users(first_name, last_name, telegram_id)
        values (?, ?, ?)
        """, (first_name, last_name, telegram_id))
        self.conn.commit()

    def get_user_lang(self, telegram_id):
        lang = self.cursor.execute("""
        select lang from users where telegram_id = ?
        """, (telegram_id,)).fetchone()
        return lang[0] if lang else "uz"
database = Database()
database.create_user_table()
