#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk  
import os

ws = Tk()
ws.title('Prikaway Pvt. Ltd.')
ws.geometry('300x400')
ws.config(bg='#345')
lbl=tk.Label(ws, text="SELECT TASK BELOW",font=('calibre',10, 'bold'))
lbl.pack(padx=10,pady=10)

def do1():
    os.system('python stock_calc.py')

def do2():
    os.system('python input_window_interface.py')

def do3():
    os.system('python mark_tc_leave.py')
    
def do4():
    os.system('python inventory_check.py')

def do5():
    os.system('python gen_bill.py')

def do6():
    os.system('python gen_bill_tc.py')
    
def do7():
    os.system('python payment_details.py')

def do8():
    os.system('python payment_summary_window.py')

def do9():
    os.system('python modify_invoice.py')
    
start = Button(
    ws,
    text='Generate Student Invoice',
    command= do2
    )

start.pack(padx=10,pady=10)

start1 = Button(
    ws,
    text='Modify Student Invoice',
    command= do9
    )

start1.pack(padx=10,pady=10)

stop = Button(
    ws,
    text='Mark Student Invoice for TC/Leave', command=do3
)
stop.pack(padx=10,pady=10)

cover = Button(
    ws,
    text='Enter Stock Inventory', command= do1
    )

cover.pack(padx=10,pady=10)

cover1 = Button(
    ws,
    text='Check Inventory Status', command=do4
    )

cover1.pack(padx=10,pady=10)

cover2 = Button(
    ws,
    text='Generate Bill to Principal (Non TC students only)', command=do5
    )

cover2.pack(padx=10,pady=10)

cover2 = Button(
    ws,
    text='Generate Bill to Principal (TC students only)', command=do6
    )

cover2.pack(padx=10,pady=10)

cover3 = Button(
    ws,
    text='Enter Work Order Payment Details', command=do7
    )

cover3.pack(padx=10,pady=10)

cover3 = Button(
    ws,
    text='Workorder & Payment Summary', command=do8
    )

cover3.pack(padx=10,pady=10)
ws.mainloop()


# In[ ]:




