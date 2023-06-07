#!/usr/bin/env python
# coding: utf-8

# In[12]:


import mysql.connector
import pandas as pd

def check1(a,b,c):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = """update master_data
                            set roll_no=%s , bill_no=%s where bill_no=%s"""
    render=tuple([a,c,b])
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,render)

    connection.commit()
    connection.close()

def check2(a):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = """update master_data
                            set student_name=%s where bill_no=%s"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,a)
    
    connection.commit()
    connection.close()
    
def check3(a):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = """update master_data
                            set class=%s where bill_no=%s"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,a)
    
    connection.commit()
    connection.close()
    
def check4(a):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = """update master_data
                            set house=%s where bill_no=%s"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,a)
    
    connection.commit()
    connection.close()
    
def check5(a):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = """update master_data
                            set item_quantity=%s , item_size=%s, total_price=%s where item_purchased=%s and bill_no=%s"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,a)
    
    connection.commit()
    connection.close()

def check5(a):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = """update master_data
                            set item_quantity=%s , item_size=%s, total_price=%s where item_purchased=%s and bill_no=%s"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,a)
    
    connection.commit()
    connection.close()
    
def check6(a):
    
    connection = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        password = "12345",
                                        database="prikaway")

    sql_select_Query = """select * from master_data m join price_list p 
                            on m.item_purchased=p.item_name where bill_no=%s"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,a)
    records=cursor.fetchall()
    a=pd.DataFrame(records)
    connection.commit()
    connection.close()
    return a


# In[ ]:




