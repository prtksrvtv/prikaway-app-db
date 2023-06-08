#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk  
import os
import mysql.connector
from datetime import datetime
from done_window import *

def do10(a,b,c,d):
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")
    sql_select_Query = """delete from master_data
                            where bill_no=%s and date_of_purchase=%s and class=%s"""
    a=name_entry1.get()
    b=name_entry2.get()
    c=name_entry3.get()
    render=tuple([a,b,c])
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,render)

    connection.commit()
    connection.close()
    yalla(d)
    
ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('300x400')
ws.config(bg='#345')

lbl=tk.Label(ws, text="DELETE BILL",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="ENTER BILL NO.",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry1 = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry1.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="ENTER BILL DATE (yyyy-mm-dd)",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry2 = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry2.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="ENTER CLASS",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry3 = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry3.pack(padx=10,pady=10)

submit = Button(
    ws,
    text='SUBMIT', command= lambda: do10(name_entry1,name_entry2,name_entry3,ws)
    )
submit.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="WARNING: BE CAREFUL! ",font=('calibre',10, 'bold'))
name_label.pack()

ws.mainloop()


# In[ ]:




