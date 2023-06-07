#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk  
import os
from db_check import *
from modify_bill import *

def do2():
    
    temp=[]
    temp.append(name_entry.get())
    real(temp)
    
ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('300x300')
ws.config(bg='#345')

lbl=tk.Label(ws, text="MODIFY BILL",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="ENTER BILL NO.",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry.pack(padx=10,pady=10)
z=name_entry.get()
submit = Button(
    ws,
    text='SUBMIT', command= do2
    )
submit.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="WARNING: ONLY DO THE CHANGES ",font=('calibre',10, 'bold'))
name_label.pack()
name_label=tk.Label(ws, text="THAT ARE NEEDED, LEAVE OTHER",font=('calibre',10, 'bold'))
name_label.pack()
name_label=tk.Label(ws, text="FIELDS BLANK IN THE NEXT",font=('calibre',10, 'bold'))
name_label.pack()
name_label=tk.Label(ws, text="WINDOW THAT APPEARS",font=('calibre',10, 'bold'))
name_label.pack()
name_label=tk.Label(ws, text="NOTICE: ALWAYS UPDATE ITEM QUANTITY",font=('calibre',10, 'bold'))
name_label.pack()
name_label=tk.Label(ws, text="AND SIZE TOGETHER",font=('calibre',10, 'bold'))
name_label.pack()
ws.mainloop()


# In[ ]:




