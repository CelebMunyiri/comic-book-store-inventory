from flask import Flask, render_template, request, redirect
from user import User
from inventory import Inventory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        user.register()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = User.get_all_users()
        for user in users:
            if user[0] == username and user[1] == password:
                return redirect('/inventory')
        return 'Invalid username or password'
    return render_template('login.html')

@app.route('/inventory')
def inventory():
    items = Inventory.get_all_items()
    return render_template('inventory.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        item = Inventory(name, quantity)
        item.add_item()
        return redirect('/inventory')
    return render_template('add.html')

@app.route('/delete/<name>')
def delete(name):
    item = Inventory(name, 0)
    item.delete_item()
    return redirect('/inventory')

if __name__ == 'main':
    app.run(debug=True)
