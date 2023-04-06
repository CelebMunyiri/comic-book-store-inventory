from tkinter import *
from tkinter import messagebox
from user import User
from inventory import Inventory

class App:
    def __init__(self, master):
        self.master = master
        master.title("Comic Inventory Management")
        master.geometry("500x300")
        
        # Create the user and inventory objects
        self.user = User()
        self.inventory = Inventory()
        
        # Create the frames
        self.login_frame = Frame(master)
        self.inventory_frame = Frame(master)
        self.add_frame = Frame(master)
        self.delete_frame = Frame(master)
        
        # Pack the frames
        self.login_frame.pack()
        self.inventory_frame.pack()
        self.add_frame.pack()
        self.delete_frame.pack()
        
        # Login frame
        self.username_label = Label(self.login_frame, text="Username:")
        self.username_label.pack(side=LEFT)
        self.username_entry = Entry(self.login_frame)
        self.username_entry.pack(side=LEFT)
        self.password_label = Label(self.login_frame, text="Password:")
        self.password_label.pack(side=LEFT)
        self.password_entry = Entry(self.login_frame, show="*")
        self.password_entry.pack(side=LEFT)
        self.login_button = Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(side=LEFT)
        self.register_button = Button(self.login_frame, text="Register", command=self.register)
        self.register_button.pack(side=LEFT)
        
        # Inventory frame
        self.inventory_label = Label(self.inventory_frame, text="Inventory")
        self.inventory_label.pack()
        self.inventory_listbox = Listbox(self.inventory_frame)
        self.inventory_listbox.pack()
        self.update_inventory()
        self.add_button = Button(self.inventory_frame, text="Add Item", command=self.show_add_frame)
        self.add_button.pack()
        self.delete_button = Button(self.inventory_frame, text="Delete Item", command=self.show_delete_frame)
        self.delete_button.pack()
        
        # Add frame
        self.add_label = Label(self.add_frame, text="Add Item")
        self.add_label.pack()
        self.add_name_label = Label(self.add_frame, text="Name:")
        self.add_name_label.pack(side=LEFT)
        self.add_name_entry = Entry(self.add_frame)
        self.add_name_entry.pack(side=LEFT)
        self.add_quantity_label = Label(self.add_frame, text="Quantity:")
        self.add_quantity_label.pack(side=LEFT)
        self.add_quantity_entry = Entry(self.add_frame)
        self.add_quantity_entry.pack(side=LEFT)
        self.add_submit_button = Button(self.add_frame, text="Add", command=self.add_item)
        self.add_submit_button.pack()
        self.add_cancel_button = Button(self.add_frame, text="Cancel", command=self.hide_add_frame)
        self.add_cancel_button.pack()
        
        # Delete frame
        self.delete_label = Label(self.delete_frame, text="Delete Item")
        self.delete_label.pack()
        self.delete_name_label = Label(self.delete_frame, text="Name:")
        self.delete_name_label.pack(side=LEFT)
        self.delete_name_entry = Entry(self.delete_frame)
        self.delete_name_entry.pack(side=LEFT)
        self.delete_submit_button = Button(self.delete_frame, text="Delete", command=self.delete_item)
        self.delete_submit_button.pack()
        self.delete_cancel_button = Button(self.delete_frame, text="Cancel", command=self.hide_delete_frame)
        self.delete_cancel_button.pack()
        
        # Hide the add and delete frames
        self.hide_add_frame()
        self.hide_delete_frame()
        
    def login(self):
        # Authenticate the user
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user.authenticate(username, password):
            # Show the inventory frame
            self.login_frame.pack_forget()
            self.inventory_frame.pack()
        else:
            messagebox.showerror("Error", "Invalid username or password.")
            
    def register(self):
        # Register a new user
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user.register(username, password):
            messagebox.showinfo("Success", "Registration successful.")
        else:
            messagebox.showerror("Error", "Registration failed.")
        
    def update_inventory(self):
        # Update the inventory listbox
        self.inventory_listbox.delete(0, END)
        for item in self.inventory.get_items():
            self.inventory_listbox.insert(END, item)

            def get_items(self):
                   return self.items

            
    def show_add_frame(self):
        # Show the add frame
        self.inventory_frame.pack_forget()
        self.add_frame.pack()
        
    def hide_add_frame(self):
        # Hide the add frame
        self.add_name_entry.delete(0, END)
        self.add_quantity_entry.delete(0, END)
        self.add_frame.pack_forget()
        self.inventory_frame.pack()
        
    def add_item(self):
        # Add an item to the inventory
        name = self.add_name_entry.get()
        quantity = self.add_quantity_entry.get()
        if self.inventory.add_item(name, quantity):
            self.update_inventory()
            self.hide_add_frame()
        else:
            messagebox.showerror("Error", "Item already exists.")
        
    def show_delete_frame(self):
        # Show the delete frame
        self.inventory_frame.pack_forget()
        self.delete_frame.pack()
        
    def hide_delete_frame(self):
        # Hide the delete frame
        self.delete_name_entry.delete(0, END)
        self.delete_frame.pack_forget()
        self.inventory_frame.pack()
        
    def delete_item(self):
        # Delete an item from the inventory
        name = self.delete_name_entry.get()
        if self.inventory.delete_item(name):
            self.update_inventory()
            self.hide_delete_frame()
        else:
            messagebox.showerror("Error", "Item does not exist.")

