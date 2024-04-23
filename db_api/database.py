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
                password TEXT,
                is_auth BOOL
            )
            """
        )
        self.con.commit()

    def register_user(self, tg_id, fullname, username, password):
        self.cur.execute(
            f"INSERT INTO users (tg_id, fullname, username, password, is_auth) VALUES ('{tg_id}', '{fullname}', '{username}', '{password}', 'True')"
        )
        self.con.commit()

    def take_users(self):
        return self.cur.execute(f"SELECT tg_id, password, is_auth FROM users").fetchall()

    def authorize_user(self, tg_id, password):
        users = self.cur.execute(f"SELECT tg_id, password FROM users").fetchall()
        for user_id, passw in users:
            user_telegramm_id = user_id
            if user_telegramm_id == tg_id:
                user_password = passw
                if user_password == password:
                    return True
        return False

    def is_auth_to_False(self, tg_id):
        self.cur.execute(f"UPDATE users SET is_auth = 'False' WHERE tg_id = '{tg_id}'")
        self.con.commit()

    def is_auth_to_True(self, tg_id):
        self.cur.execute(f"UPDATE users SET is_auth = 'True' WHERE tg_id = '{tg_id}'")
        self.con.commit()
