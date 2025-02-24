import pymysql
from tkinter import messagebox
def connect_db():
    global mycursor,c
    try:
        c=pymysql.connect(host ='localhost',user='root',password='KaVyAs@23082003')
        mycursor=c.cursor()
    except:
        messagebox.showerror('Error','Something went wrong')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS EMPLOYEE_DATA')
    mycursor.execute('USE EMPLOYEE_DATA')
    mycursor.execute('CREATE TABLE IF NOT EXISTS DATA(ID VARCHAR(30),NAME VARCHAR(30),PHONE VARCHAR(15),ROLE VARCHAR(50),GENDER VARCHAR(10),SALARY DECIMAL(10,2))')

def insert(id,name,phone,salary,role,gender):
    mycursor.execute('INSERT INTO DATA VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    c.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM DATA WHERE ID=%s',id)
    result = mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('Select * from DATA')
    res=mycursor.fetchall()
    return res

def update(id,new_name,new_phone,new_salary,new_role,new_gender):
    mycursor.execute('UPDATE DATA SET NAME=%s,PHONE=%s,ROLE=%s,GENDER=%s,SALARY=%s WHERE ID=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    c.commit()

def delete(id):
    mycursor.execute('DELETE FROM DATA WHERE ID=%s',id)
    c.commit()

def del_all():
    mycursor.execute('DELETE FROM DATA')
    c.commit()

def search(option,val):
    mycursor.execute(f'SELECT * FROM DATA WHERE {option}=%s',val)
    return mycursor.fetchall()
connect_db()