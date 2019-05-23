import tkinter as tk
from dbbase import signup , login


main_frame = tk.Tk()
main_frame.title("Authentication")
main_frame.geometry("550x220+30+30")
main_frame.iconbitmap(default='icon.ico')


def login_gui(main_frame):
	root = tk.Frame(main_frame,bg = "cyan")
	root.place(x=0,y=0,width = 550, height = 220)
	tk.Label(root,text = "Our First Gui Authentication",fg= "blue",bg = "pink",font=("monaco",22,"bold")).place(x = 10,y = 20)
	tk.Label(root,text = "Enter Your User Id",bg = "cyan",font=("monaco",10,"bold")).place(x = 10,y= 80)
	userid = tk.Entry(root,font=("monaco",10,"bold"))
	userid.place(x = 190,y=80,width=150)
	tk.Label(root,text = "Enter Your Password",bg = "cyan",font=("monaco",10,"bold")).place(x = 10,y= 120)
	password = tk.Entry(root,show="*",font=("monaco",10,"bold"))
	password.place(x = 190,y=120,width=150)
	login_button = tk.Button(root,text ="Login",font=("monaco",20,"bold"),bg = "white",fg = "green",command = lambda :login(userid,password,root,main_frame))
	login_button.place(x = 355,y = 85, height = 110, width = 180)
	Signup_button = tk.Button(root,text ="Signup",font=("monaco",10,"bold"),bg = "white",fg = "green",command = lambda :signup_gui(root))
	Signup_button.place(x = 10,y = 180, height = 30, width = 60)

def signup_gui(frame):
	frame.destroy()
	frame = tk.Frame(main_frame,bg = "cyan")
	frame.place(x=0,y=0,width = 550, height = 220)
	tk.Label(frame,text = "New User Registration",fg= "blue",bg = "pink",font=("monaco",22,"bold")).place(x = 60,y = 10)
	tk.Label(frame,text = "Enter New User Id",bg = "cyan",font=("monaco",10,"bold")).place(x = 10,y= 80)
	userid = tk.Entry(frame,font=("monaco",10,"bold"))
	userid.place(x = 190,y=80,width=150)
	tk.Label(frame,text = "Enter New Password",bg = "cyan",font=("monaco",10,"bold")).place(x = 10,y= 115)
	password = tk.Entry(frame,show="*",font=("monaco",10,"bold"))
	password.place(x = 190,y=115,width=150)
	tk.Label(frame,text = "Enter Your Name",bg = "cyan",font=("monaco",10,"bold")).place(x = 10,y= 150)
	name = tk.Entry(frame,font=("monaco",10,"bold"))
	name.place(x = 190,y=150,width=150)
	signup_button = tk.Button(frame,text ="Signup",font=("monaco",20,"bold"),bg = "white",fg = "green",command = lambda :signup(userid,password,name,frame,main_frame,login_gui))
	signup_button.place(x = 355,y = 85, height = 110, width = 180)
	Login_button = tk.Button(frame,text ="Login Page",font=("monaco",10,"bold"),bg = "white",fg = "green",command = lambda :login_gui(main_frame))
	Login_button.place(x = 10,y = 180, height = 30, width = 100)


login_gui(main_frame)
main_frame.mainloop()
