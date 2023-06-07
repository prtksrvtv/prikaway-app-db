#!/usr/bin/env python
# coding: utf-8

# In[14]:


import mysql.connector
import pandas as pd

def upd(bill):
    print(bill)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database="prikaway"
    )
    cursor = mydb.cursor()
    query = """update master_data m
                set m.tc_leave= True
                where bill_no=%s"""
    cursor.execute(query,bill)
    cursor.execute("select distinct(bill_no) from master_data")
    a=pd.DataFrame(cursor.fetchall())
    mydb.commit()
    mydb.close()
    z=a[0].loc[(a[0]==bill[0])]
    if len(z.values)>0:
        return True
    else:
        return False


# In[ ]:




