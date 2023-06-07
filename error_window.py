#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk

def destro(n):
    ws = Tk()
    ws.title('Prikaway Pvt. Ltd.')
    ws.geometry('300x100')
    ws.config(bg='#345')
    lbl=tk.Label(ws, text="Error! Relaunch and Try Again ",font=('calibre',10, 'bold'))
    lbl.pack(padx=10,pady=10)
    but=Button(ws, text="Quit", command=lambda: [n.destroy(), ws.destroy()])
    but.pack(padx=10,pady=10)
    ws.mainloop()

    


# In[ ]:




