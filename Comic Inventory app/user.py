# user.py
import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def register(self):
        conn = sqlite3.connect('comic_store.db')
        c = conn.cursor()
        c.execute('INSERT INTO users VALUES (?, ?)', (self.username, self.password))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_all_users():
        conn = sqlite3.connect('comic_store.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        users = c.fetchall()
        conn.close()
        return users


