# inventory.py
import sqlite3

class Inventory:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        
    def add_item(self):
        conn = sqlite3.connect('comic_store.db')
        c = conn.cursor()
        c.execute('INSERT INTO inventory VALUES (?, ?)', (self.name, self.quantity))
        conn.commit()
        conn.close()
        
    def delete_item(self):
        conn = sqlite3.connect('comic_store.db')
        c = conn.cursor()
        c.execute('DELETE FROM inventory WHERE name=?', (self.name,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_all_items():
        conn = sqlite3.connect('comic_store.db')
        c = conn.cursor()
        c.execute('SELECT * FROM inventory')
        items = c.fetchall()
        conn.close()
        return items