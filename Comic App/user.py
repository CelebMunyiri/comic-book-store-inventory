import sqlite3

class User:
    def __init__(self):
        self.conn = sqlite3.connect('comic_inventory.db')
        self.c = self.conn.cursor()
        
    def register(self, username, password):
        # Insert the new user into the database
        try:
            self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # If the username already exists, return False
            return False
        
    def login(self, username, password):
        # Check if the username and password match
        self.c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.c.fetchone()
        if user:
            return True
        else:
            return False
