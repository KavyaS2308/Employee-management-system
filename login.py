from customtkinter import *
from PIL import Image
from tkinter import messagebox
#define login command
def login():
    if username.get()=='' or password.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif username.get()=='kavya' and password.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong Credentials')
# Create login page
root = CTk()
root.geometry('850x460')
root.resizable(0,0)
root.title("login page")
#add background image
image = CTkImage(Image.open('background.jpg'),size=(850,460))
imageLabel = CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
#add title
h = CTkLabel(root,text ='Employee Login page',bg_color='#5DA3DE', font=('Times New Roman',20,'bold'))
h.place(x=103,y=50)
#add username entry box
user = CTkLabel(root,text ='Username*',bg_color='#5DA3DE', font=('Times New Roman',15,'bold'))
user.place(x=109,y=125)
username=CTkEntry(root,placeholder_text='Enter your Username',bg_color='#5DA3DE',width=180)
username.place(x=105,y=150)
#add password entry box
pw = CTkLabel(root,text ='Password*',bg_color='#5DA3DE', font=('Times New Roman',15,'bold'))
pw.place(x=109,y=195)
password=CTkEntry(root,placeholder_text='Enter your Password',bg_color='#5DA3DE',width=180,show='*')
password.place(x=105,y=220)
#add login page
loginbtn=CTkButton(root,text='login',bg_color='#5DA3DE',fg_color='#A6CBED',text_color='black',font=('Times New Roman',15,'bold'),width=110,height=30,cursor='hand2',command=login)
loginbtn.place(x=140,y=290)
root.mainloop()


