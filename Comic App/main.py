from tkinter import Tk
from app import App

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()


def ShowRegisterForm():
    global registerform
    registerform = Toplevel()
    registerform.title("Comic book store/Account Register")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    registerform.resizable(0, 0)
    registerform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    RegisterForm()
    
def RegisterForm():
    global lbl_result
    TopRegisterForm = Frame(registerform, width=600, height=100, bd=1, relief=SOLID)
    TopRegisterForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopRegisterForm, text="User Registration", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidRegisterForm = Frame(registerform, width=600)
    MidRegisterForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidRegisterForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidRegisterForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidRegisterForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidRegisterForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidRegisterForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_register = Button(MidRegisterForm, text="Register", font=('arial', 18), width=30, command=Register)
    btn_register.grid(row=2, columnspan=2, pady=20)
    btn_register.bind('<Return>', Register)

    def regist(event=None):
          global admin_id  
Database()
if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete all fields!", fg="red")
else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result.config(text="Username already exists!", fg="red")
        else:
            cursor.execute("INSERT INTO `admin` (username, password) VALUES(?, ?)",
                           (USERNAME.get(), PASSWORD.get()))
            conn.commit()
            lbl_result.config(text="User registered successfully!", fg="green")
            USERNAME.set("")
            PASSWORD.set("")
cursor.close()
conn.close()
