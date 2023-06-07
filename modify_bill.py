#!/usr/bin/env python
# coding: utf-8

# In[13]:


from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
from invpro import *
from dbin import *
from tkinter.ttk import *
import mysql.connector
from datetime import date
from db_check import *
import os
from stock_mod import *
from correct_new_invoice import *
from error_window import *
from done_window import *

def real(w):
    connection = mysql.connector.connect(
                                            host = "localhost",
                                            user = "root",
                                            password = "12345",
                                            database="prikaway")

    sql_select_Query = "select * from price_list"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    a=pd.DataFrame(records)
    sql_select_Query = "select item_purchased,item_size,item_quantity from master_data where bill_no=%s"
    cursor.execute(sql_select_Query,w)
    # get all records
    records = cursor.fetchall()
    t=pd.DataFrame(records)
    sql_select_Query = "select * from inventory"
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    inv=pd.DataFrame(records)
    items=['Roll No.','Name','Class','House','Date']
    d={}

    for y in items:
        d[y]=''
    for y in a.iterrows():
        d[y[1][0]] = 0



    root=Tk()
    root.title("Input the item qunatity")
    # setting the windows size
    root.geometry("600x600")
    main_frame=Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame, anchor='nw')
    count=0
    
    for x in d:

        if x not in ['Roll No.','Name','Class','House','Date']:
            name_label = tk.Label(second_frame, text = x, font=('calibre',10, 'bold'))
            name_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
            size_label=tk.Label(second_frame, text = 'Size', font=('calibre',10, 'bold'))
            size_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
            size_label.grid(row=count,column=2)
            size_entry.grid(row=count,column=3)
            d[x]=[name_entry,size_entry]
            name_label.grid(row=count,column=0)
            name_entry.grid(row=count,column=1)
        else:
            name_label = tk.Label(second_frame, text = x, font=('calibre',10, 'bold'))
            name_entry = tk.Entry(second_frame, font=('calibre',10,'normal'))
            d[x]=name_entry
            name_label.grid(row=count,column=0)
            name_entry.grid(row=count,column=1)

        count+=1

    submit = Button(
        second_frame,
        text='Print', command= lambda : rty(a,t,d,w,inv,root)
        )
    submit.grid(row=count,column=0)

    def rty(a,t,d,w,inv,root):

        for x in d:
            if x not in ['Roll No.','Name','Class','House','Date']:
                if d[x][0].get()=='':
                    d[x][0]='Not'
                    d[x][1]='Not'
                else:
                    d[x][0]=d[x][0].get()
                    d[x][1]=d[x][1].get()
                    
            else:
                if d[x].get()=='':
                    d[x]='Not'           
                else:
                    d[x]=d[x].get()
        lamb={}
        for x in d:
            if x not in ['Roll No.','Name','Class','House','Date']:
                if d[x][0]=='Not' and d[x][1]=='Not':
                    continue
                else:
                    lamb[x]=[d[x][0],d[x][1]]
            else:
                if d[x]=='Not':
                    continue
                else:
                    lamb[x]=d[x]
        
        try:
            for x in lamb:
                if x not in ['Roll No.','Name','Class','House','Date']:
                    if type(int(lamb[x][0])) is int:
                        continue
        except ValueError:
            destro(root)
        
        for x in lamb:
            if x=='House':
                if lamb[x].lower()=='a':
                    lamb[x]='Arjan'
                if lamb[x].lower()=='c':
                    lamb[x]='Cariappa'
                if lamb[x].lower()=='k':
                    lamb[x]='Katari'
                if lamb[x].lower()=='m':
                    lamb[x]='Manekshaw'
                if lamb[x].lower()=='p':
                    lamb[x]='Pereira'
                if lamb[x].lower()=='s':
                    lamb[x]='Subroto'
                if lamb[x].lower()=='r':
                    lamb[x]='Rezangla'
                else:
                    raise Exception(destro(root))
            else:
                continue
        
        flag=0
        for x in lamb:
            if x=='Roll No.':
                today_date=date.today()
                new="PWPL/RW/"+today_date.strftime("%y")+"/"+today_date.strftime("%b")+"/"+lamb[x]
                flag=1
                check1(lamb[x],w[0],new)    
            elif x=='Name':
                render=tuple([lamb[x],w[0]])
                check2(render)
            elif x=='Class':
                render=tuple([lamb[x],w[0]])
                check3(render)
            elif x=='House':
                render=tuple([lamb[x],w[0]])
                check4(render)
            else:
                for y in a.iterrows():
                    if x==y[1][0]:
                        total=y[1][1]*int(lamb[x][0])
                        break
                for y in t.iterrows():
                    if x==y[1][0]:
                        diff=y[1][2]-int(lamb[x][0])
                        break
                render=tuple([lamb[x][0],lamb[x][1],total,x,w[0]])
                check5(render) 
                for z in inv.iterrows():
                    if z[1][0]==x and z[1][2]==lamb[x][1]:
                        v=z[1][1]+diff
                        break
                roger1(tuple([v,x,lamb[x][1]]))
        
        if flag==1:
            render=tuple([new])
            ring=check6(render)
        else:
            render=tuple([w[0]])
            ring=check6(render)
        gill(ring) 
        yalla(root)
    root.mainloop()


# In[ ]:




