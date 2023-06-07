#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gill(a):
    from numtoword import number_to_word
    from fpdf import FPDF
    from prettytable import PrettyTable
    from PIL import Image, ImageDraw, ImageFont
    import datetime
    import os
    import subprocess
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B",size = 10)
    
    for x in os.listdir(os.getcwd()):
        if x == 'PRIKAWAY_REWARI_LOGO.png':
            path=os.getcwd()+'\\'+x
            break
            
    j=PrettyTable()
    j.add_column('Roll No.',[a[0][0]])
    j.add_column('Name.',[a[1][0]])
    j.add_column('Class',[a[2][0]])
    j.add_column('House',[a[3][0]])
    j.add_column('Date',[a[9][0]])
    currentMonth = datetime.datetime.now()
    j.add_column('Invoice No.',[a[10][0]])
    im = Image.new("RGB", (600, 70), "white")
    draw = ImageDraw.Draw(im)
    font = ImageFont.load_default()
    draw.text((0, 0), str(j), font=font, fill="black")
    im.save("header for roll no_"+str(a[0][0])+".png")
    pdf.image(path, w=190, h=15)
    pdf.image("header for roll no_"+str(a[0][0])+".png", w=193, h=20)
    
    j=PrettyTable(['Item Purchased','Size','Price','Quantity','Total'])
    price=count=0
    
    for x in a.iterrows():
        j.add_row([x[1][4],x[1][5],x[1][12],x[1][6],x[1][7]])
        count=count+int(x[1][6])
        price=price+int(x[1][7])
        
    j.add_row(['-'*38,'-'*4,'-'*5,'-'*8,'-'*6])
    j.add_row(['Grand Total','','',count,"{:,}".format(price)])
    j.align["Item Purchased"]="l"
    j.align["Size"]="l"
    j.align["Quantity"]="r"
    j.align["Price"]="r"
    j.align["Total"]="r"
    ip = Image.new("RGB", (480, 900), "white")
    draw = ImageDraw.Draw(ip)
    font = ImageFont.load_default()
    draw.text((0, 0), str(j), font=font, fill="black")
    ip.save("table for roll no_"+str(a[0][0])+".png")
    pdf.image("table for roll no_"+str(a[0][0])+".png", w=195, h=224)
    pdf.set_font("Arial", style="B",size = 10)
    pdf.cell(200, 3, txt = "AMOUNT PAYABLE(In Words):"+'\t'*5+number_to_word(price),ln = 1, align = 'L')
    pdf.set_font("Arial", size = 8)
    pdf.cell(200, 2, txt = "-"*200,ln = 1, align = 'L')
    pdf.cell(200, 2, txt = "CADET'S SIGNATURE"+'\t'*55+"HOUSE MASTER SIGNATURE"+'\t'*50+"AUTHORISED SIGNATURE",ln = 1, align = 'L')
    pdf.output("Invoice for roll_no_"+str(a[0][0])+".pdf")
    pa_check="Invoice for roll_no_"+str(a[0][0])+".pdf"
    os.remove("header for roll no_"+str(a[0][0])+".png")
    os.remove("table for roll no_"+str(a[0][0])+".png")
    path=os.getcwd()+'\\Result\\'
    if os.path.exists(path+'Invoice for roll_no_'+str(a[0][0])+'.pdf'):
        os.remove(path+'Invoice for roll_no_'+str(a[0][0])+'.pdf')
    os.rename(os.getcwd()+'\\Invoice for roll_no_'+str(a[0][0])+'.pdf', path+'Invoice for roll_no_'+str(a[0][0])+'.pdf')
    subprocess.Popen([path+'Invoice for roll_no_'+str(a[0][0])+'.pdf'],shell=True)


# In[ ]:




