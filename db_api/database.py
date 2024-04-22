import sqlite3


class DataBase:
    def __init__(self, name):
        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                tg_id INTEGER,
                fullname TEXT,
                username TEXT,
                password TEXT
            )
            """
        )
        self.con.commit()

    def register_user(self, tg_id, fullname, username):
        self.cur.execute(
            f"INSERT INTO users (tg_id, fullname, username) VALUES ('{tg_id}', '{fullname}', '{username}')"
        )
        self.con.commit()

    def authorize_user(self, tg_id, password):
        users = self.cur.execute(f"SELECT tg_id, password FROM users").fetchall()[0]
        for user_content in users:
            user_telegramm_id = user_content[0]
            if user_telegramm_id == tg_id:
                user_password = user_content[1]
                if user_password == password:
                    return True
        return False
