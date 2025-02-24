from customtkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import db
#functions
def clear(val=False):
    if val:
        tree.selection_remove(tree.focus())
    identry.delete(0,END)
    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    salaryentry.delete(0,END)
    rolebox.set('')
    genderbox.set('')
def selection(e):
    selected=tree.selection()
    if selected:
        row=tree.item(selected)['values']
        clear()
        identry.insert(0,row[0])
        nameentry.insert(0,row[1])
        phoneentry.insert(0,row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryentry.insert(0,row[5])

def tree_view():
    emp=db.fetch_employees()
    tree.delete(*tree.get_children())
    for e in emp:
        tree.insert('',END,values=e)
def add_employee():
    if identry.get()=='' or nameentry.get()=='' or phoneentry.get()=='' or salaryentry.get()=='' or rolebox.get()=='' or genderbox.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif db.id_exists(identry.get()):
        messagebox.showerror('Error','Id already exists')
    elif not identry.get().startswith('EMP'):
        messagebox.showerror('Error', 'Invalid ID format. Please provide valid Id')
    else:
        db.insert(identry.get(),nameentry.get(),phoneentry.get(),salaryentry.get(),rolebox.get(),genderbox.get())
        messagebox.showinfo('Success','Data is successfully added')
        clear()
        tree_view()
def update_employee():
    selected=tree.selection()
    if not selected:
        messagebox.showerror('Error','Select data to update')
    else:
        db.update(identry.get(),nameentry.get(),phoneentry.get(),salaryentry.get(),rolebox.get(),genderbox.get())
        tree_view()
        clear()
        messagebox.showinfo('Success','Data is updated successfully')
def delete_employee():
    selected=tree.selection()
    if not selected:
        messagebox.showerror('Error','Select data to delete')
    else:
        db.delete(identry.get())
        tree_view()
        clear()
        messagebox.showinfo('Success', 'Data of the selected employee is deleted successfully')
def delete_all():
    res=messagebox.askyesno('Confirm','All records will be deleted. Are you sure?')
    if res:
        db.del_all()
        tree_view()
        clear()
        messagebox.showinfo('Success', 'All data is deleted successfully')
def search_Employee():
    if searchentry.get()=='' or searchbox.get()=='Search By':
        messagebox.showerror('Error','Please select an option and enter value to search')
    else:
        search=db.search(searchbox.get(),searchentry.get())
        tree.delete(*tree.get_children())
        for e in search:
            tree.insert('', END, values=e)
def show_all():
    tree_view()
    searchentry.delete(0,END)
    searchbox.set('Search By')
#create ems window
window=CTk()
window.title('Employee Management system')
window.geometry('940x600+100+100')
window.resizable(0,0)
window.configure(fg_color='#F5EFFF')
#add background image
img=CTkImage(Image.open('ems_bg.jpg'),size=(940,200))
imgLabel = CTkLabel(window,image=img,text='')
imgLabel.grid(row=0,column=0,columnspan=2)
#create frame(containers) to add label, field and buttons
#left frame
lframe=CTkFrame(window,fg_color="#F5EFFF")
lframe.grid(row=1,column=0)

#field name
idLabel=CTkLabel(lframe,text="Id:",font=("Times New Roman",18,'bold'))
idLabel.grid(row=0,column=0,padx=(0,5),pady=(15),sticky='w')

nameLabel=CTkLabel(lframe,text="Name:",font=("Times New Roman",18,'bold'))
nameLabel.grid(row=1,column=0,padx=(0,5),pady=(15),sticky='w')

phoneLabel=CTkLabel(lframe,text="Phone number:",font=("Times New Roman",18,'bold'))
phoneLabel.grid(row=2,column=0,padx=(0,5),pady=(15),sticky='w')

roleLabel=CTkLabel(lframe,text="Role:",font=("Times New Roman",18,'bold'))
roleLabel.grid(row=3,column=0,padx=(0,5),pady=(15),sticky='w')

genderLabel=CTkLabel(lframe,text="Gender:",font=("Times New Roman",18,'bold'))
genderLabel.grid(row=4,column=0,padx=(0,5),pady=(15),sticky='w')

salaryLabel=CTkLabel(lframe,text="Salary:",font=("Times New Roman",18,'bold'))
salaryLabel.grid(row=5,column=0,padx=(0,5),pady=(15),sticky='w')
#entry field
identry=CTkEntry(lframe,font=("Times New Roman",15,'bold'),width=180)
identry.grid(row=0,column=1,padx=(0,5))

nameentry=CTkEntry(lframe,font=("Times New Roman",15,'bold'),width=180)
nameentry.grid(row=1,column=1)

phoneentry=CTkEntry(lframe,font=("Times New Roman",15,'bold'),width=180)
phoneentry.grid(row=2,column=1)

#combo box for role
options=['Software Developer','Web Developer','Data Scientist','UI/UX Designer','Front-end Developer','Backend Developer','Business Analyst','Cloud Engineer']
rolebox=CTkComboBox(lframe,values=options,width=180,font=("Times New Roman",15,'bold'),state='readonly')
rolebox.grid(row=3,column=1)

#combo box for gender
options_2=['Male','Female']
genderbox=CTkComboBox(lframe,values=options_2,width=180,font=("Times New Roman",15,'bold'),state='readonly')
genderbox.grid(row=4,column=1)

salaryentry=CTkEntry(lframe,font=("Times New Roman",15,'bold'),width=180)
salaryentry.grid(row=5,column=1)
#right frame
rframe=CTkFrame(window,fg_color='#CCA6FB')
rframe.grid(row=1,column=1)

options_3=['Id','Name','Phone','Role','Gender','Salary']
searchbox=CTkComboBox(rframe,values=options_3,state='readonly')
searchbox.grid(row=0,column=0)
searchbox.set('Search By')

searchentry=CTkEntry(rframe,font=("Times New Roman",15,'bold'))
searchentry.grid(row=0,column=1)

searchbtn = CTkButton(rframe,text='Search',fg_color='#8356B9',width=95,command=search_Employee)
searchbtn.grid(row=0,column=2)

showallbtn = CTkButton(rframe,text='Show All',fg_color='#8356B9',width=95,command=show_all)
showallbtn.grid(row=0,column=3,pady=5)

tree= ttk.Treeview(rframe,height=10)
tree.grid(row=1,column=0,columnspan=4)
tree['columns']=('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Salary',text='Salary')
tree.heading('Gender',text='Gender')
tree.config(show='headings')
tree.column('Id',anchor=CENTER,width=50)
tree.column('Name',anchor=CENTER,width=160)
tree.column('Phone',anchor=CENTER,width=110)
tree.column('Role',anchor=CENTER,width=190)
tree.column('Salary',anchor=CENTER,width=90)
tree.column('Gender',anchor=CENTER,width=120)
style=ttk.Style()
style.configure('Treeview.Heading',font=('Times New Roman',15,'bold'))
style.configure('Treeview',font=('Times New Roman',15,'bold'),rowheight=30,background='#E8D6FE')

scrollbar=ttk.Scrollbar(rframe,orient=VERTICAL,command=tree.yview())
scrollbar.grid(row=1,column=4,sticky='ns')
tree.config(yscrollcommand=scrollbar.set)
#button frame
bframe=CTkFrame(window,fg_color="#CCA6FB")
bframe.grid(row=2,column=0,columnspan=2)

newbtn=CTkButton(bframe,text='New Employee',fg_color='#8356B9',font=('Times New Roman',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newbtn.grid(row=0,column=0,pady=5)
addbtn=CTkButton(bframe,text='Add Employee',fg_color='#8356B9',font=('Times New Roman',15,'bold'),width=160,corner_radius=15,command=add_employee)
addbtn.grid(row=0,column=1,pady=5,padx=5)
updatebtn=CTkButton(bframe,text='Update Employee',fg_color='#8356B9',font=('Times New Roman',15,'bold'),width=160,corner_radius=15,command=update_employee)
updatebtn.grid(row=0,column=2,pady=5,padx=5)
deletebtn=CTkButton(bframe,text='Delete Employee',fg_color='#8356B9',font=('Times New Roman',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deletebtn.grid(row=0,column=3,pady=5,padx=5)
deleteallbtn=CTkButton(bframe,text='Delete All',fg_color='#8356B9',font=('Times New Roman',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallbtn.grid(row=0,column=4,pady=5,padx=5)

tree_view()
window.bind('<ButtonRelease>',selection)
window.mainloop()