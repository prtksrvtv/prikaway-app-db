#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk  
from update_non_tc import *
import os
from error_window import *
from done_window import *

def do11(ws):
    
    n=[name_entry.get()]
    r=upd(n)
    print(r)
    if r==True:
        yalla(ws)
    else:
        destro(ws)
ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('300x300')
ws.config(bg='#345')
lbl=tk.Label(ws, text="MARK TC BILL TO NON TC/LEAVE",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="ENTER BILL NO.",font=('calibre',10, 'bold'))
name_label.pack(padx=10,pady=10)
name_entry = tk.Entry(ws, font=('calibre',10,'normal'))
name_entry.pack(padx=10,pady=10)
z=name_entry.get()
submit = Button(
    ws,
    text='SUBMIT', command= lambda: do11(ws)
    )
submit.pack(padx=10,pady=10)
name_label=tk.Label(ws, text="WARNING: BE CAREFUL!",font=('calibre',10, 'bold'))
name_label.pack()
ws.mainloop()


# In[ ]:




