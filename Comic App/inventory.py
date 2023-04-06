import sqlite3

class Inventory:
    def __init__(self):
        self.conn = sqlite3.connect('comic_inventory.db')
        self.c = self.conn.cursor()
        
    def view_inventory(self):
        # Select all inventory items and return them as a list of tuples
        self.c.execute("SELECT * FROM inventory")
        inventory = self.c.fetchall()
        return inventory
        
    def add_item(self, name, quantity):
        # Insert the new item into the database
        try:
            self.c.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # If the item already exists, update the quantity
            self.c.execute("UPDATE inventory SET quantity = quantity + ? WHERE name = ?", (quantity, name))
            self.conn.commit()
            return False
        
    def delete_item(self, name):
        # Delete the item from the database
        self.c.execute("DELETE FROM inventory WHERE name = ?", (name,))
        self.conn.commit()

        def get_items(self):
            return self.items
