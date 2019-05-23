import sqlite3
import tkinter as tk


def signup(userid,password,name,root,main_frame,login_gui):
    user_id = str(userid.get())
    password_d = str(password.get())
    name_d = str(name.get())
    userid.delete(0,"end")
    password.delete(0,"end")
    name.delete(0,"end")
    conn = sqlite3.connect('user.db')
    conn.execute("INSERT INTO Authentication (USERID,PASSWORD,NAME) VALUES ('{}','{}','{}')".format(user_id,password_d,name_d))
    conn.commit()
    conn.close()
    root.destroy()
    frame = tk.Frame(main_frame) 
    frame.place(x=0,y=0,width = 550, height = 220)
    tk.Label(frame,text = "Registration successfull",fg= "blue",bg = "pink",font=("monaco",22,"bold")).place(x = 60,y = 10)  


def login(userid,password,root,main_frame):
    user_id = userid.get()
    password_d = password.get()
    conn = sqlite3.connect("user.db")
    try:
        data = conn.execute("SELECT PASSWORD,NAME from Authentication Where USERID = '{}'".format(user_id)) 
        passw = str(data.fetchall()[0][0])
        if passw == password_d:
            print("login successfull")
            root.destroy()
            frame = tk.Frame(main_frame) 
            frame.place(x=0,y=0,width = 550, height = 220)
            tk.Label(frame,text = "login successfull",fg= "blue",font=("monaco",22,"bold")).place(x = 60,y = 10)  

        else:
            tk.Label(root,text="wrong password",fg="red").place(x= 50,y=150,width=220)
    except:
        tk.Label(root,text="userid does not exist",fg="red").place(x=50,y=150,width=220)
