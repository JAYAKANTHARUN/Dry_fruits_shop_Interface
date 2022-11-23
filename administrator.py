from tkinter.ttk import *
from tkinter import messagebox
import PROJECT as P
from tkinter import *
import customer as c
from PIL import ImageTk,Image

root=Tk()

root.title("DRY FRUIT SHOP")
root.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
root.geometry("350x400")
code1=StringVar()
name1=StringVar()
price1=StringVar()
quantity1=StringVar()
unm=StringVar()
pwd=StringVar()

def tkadd():
    L=[]
    c=code1.get()
    n=name1.get()
    p=price1.get()
    q=quantity1.get()
    L=[int(c),n,float(p),float(q)]
    P.add(L)
    messagebox.showinfo("Success","RECORD SAVED")

def tkdelete():
    L=[]
    c=code1.get()
    L=[int(c)]
    P.delete(L)
    messagebox.showinfo("Success","RECORD DELETED")
    
def tkupdatename():
    L=[]
    c=code1.get()
    n=name1.get()
    L=[int(c),n]
    P.updatename(L)
    messagebox.showinfo("Success","UPDATION COMPLETED")
    
def tkupdateprice():
    L=[]
    c=code1.get()
    p=price1.get()
    L=[int(c),float(p)]
    P.updateprice(L)
    messagebox.showinfo("Success","UPDATION COMPLETED")
    
def tkupdatequantity():
    L=[]
    c=code1.get()
    q=quantity1.get()
    L=[int(c),float(q)]
    P.updatequantity(L)
    messagebox.showinfo("Success","UPDATION COMPLETED")
    
def tksearch():
    L=[]
    c=code1.get()
    L=[int(c)]
    a=P.search(L)
    top=Toplevel()
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    tv=Treeview(top,columns=(1,2,3,4),show="headings",height="10")
    tv.grid(row=1,column=0)
    tv.heading(1,text="Code")
    tv.heading(2,text="Item Name")
    tv.heading(3,text="Price")
    tv.heading(4,text="Quantity")
    for i in a:
        tv.insert("","end",values=i)
    
def add_window():
    top=Toplevel()
    top.geometry("400x200")
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    l1=Label(top,text="ENTER ITEM CODE         ",font=("AgencyFB","12","bold"),bg="#FFFF66")
    l1.grid(row=0,column=0)
    e1=Entry(top,textvariable=code1,width=25)
    e1.grid(row=0,column=1)
    l2=Label(top,text="ENTER ITEM NAME         ",font=("AgencyFB","12","bold"),bg="#FFFF66")
    l2.grid(row=1,column=0)
    e2=Entry(top,textvariable=name1,width=25)
    e2.grid(row=1,column=1)
    l3=Label(top,text="ENTER PRICE PER KG  ",font=("AgencyFB","12","bold"),bg="#FFFF66")
    l3.grid(row=2,column=0)
    e3=Entry(top,textvariable=price1,width=25)
    e3.grid(row=2,column=1)
    l4=Label(top,text="ENTER QUANTITY IN KG",font=("AgencyFB","12","bold"),bg="#FFFF66")
    l4.grid(row=3,column=0)
    e4=Entry(top,textvariable=quantity1,width=25)
    e4.grid(row=3,column=1)
    b1=Button(top,text=" ADD ",command=tkadd,font=("AgencyFB","12","bold"),bg="#00CCFF")
    b1.grid(row=4,column=1)

def delete_window():
    top=Toplevel()
    top.geometry("350x100")
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    l1=Label(top,text="ENTER ITEM CODE     ",font=("AgencyFB","12","bold"),bg="#66FF66")
    l1.grid(row=0,column=0)
    e1=Entry(top,textvariable=code1)
    e1.grid(row=0,column=1)
    b1=Button(top,text=" DELETE ",command=tkdelete,font=("AgencyFB","11","bold"),bg="#FF0000")
    b1.grid(row=1,column=1)
    
def updatename_window():
    top=Toplevel()
    top.geometry("410x110")
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    l1=Label(top,text="ENTER ITEM CODE                ",font=("AgencyFB","12","bold"),bg="#FF99FF")
    l1.grid(row=0,column=0)
    e1=Entry(top,textvariable=code1)
    e1.grid(row=0,column=1)
    l2=Label(top,text="ENTER NEW ITEM NAME     ",font=("AgencyFB","12","bold"),bg="#FF99FF")
    l2.grid(row=1,column=0)
    e2=Entry(top,textvariable=name1)
    e2.grid(row=1,column=1)
    b1=Button(top,text=" UPDATE NAME ",command=tkupdatename,font=("AgencyFB","11","bold"),bg="#66FF66")
    b1.grid(row=2,column=1)
    
def updateprice_window():
    top=Toplevel()
    top.geometry("410x110")
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    l1=Label(top,text="ENTER ITEM CODE     ",font=("AgencyFB","12","bold"),bg="#FFCC00")
    l1.grid(row=0,column=0)
    e1=Entry(top,textvariable=code1)
    e1.grid(row=0,column=1)
    l3=Label(top,text="ENTER NEW PRICE PER KG  ",font=("AgencyFB","12","bold"),bg="#FFCC00")
    l3.grid(row=2,column=0)
    e3=Entry(top,textvariable=price1)
    e3.grid(row=2,column=1)
    b1=Button(top,text=" UPDATE PRICE ",command=tkupdateprice,font=("AgencyFB","11","bold"),bg="#FF6633")
    b1.grid(row=3,column=1)
    
def updatequantity_window():
    top=Toplevel()
    top.geometry("610x110")
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    l1=Label(top,text="ENTER ITEM CODE                    ",font=("AgencyFB","12","bold"),bg="#00CCFF")
    l1.grid(row=0,column=0)
    e1=Entry(top,textvariable=code1)
    e1.grid(row=0,column=1)
    l4=Label(top,text="ENTER QUANTITY IN KG THAT SHOULD BE ADDED",font=("AgencyFB","12","bold"),bg="#00CCFF")
    l4.grid(row=1,column=0)
    e4=Entry(top,textvariable=quantity1)
    e4.grid(row=1,column=1)
    b1=Button(top,text=" UPDATE QUANTITY ",command=tkupdatequantity,font=("AgencyFB","11","bold"),bg="#66FF66")
    b1.grid(row=2,column=1)
    
def display_window():
    a=P.display()
    top=Toplevel()
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    tv=Treeview(top,columns=(1,2,3,4),show="headings",height="20")
    tv.grid(row=1,column=0)
    tv.heading(1,text="CODE")
    tv.heading(2,text="ITEM NAME")
    tv.heading(3,text="PRICE PER KG")
    tv.heading(4,text="QUANTITY IN KG")
    for i in a:
        tv.insert("","end",values=i)    
        
def search_window():
    top=Toplevel()
    top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    top.geometry("310x110")
    l1=Label(top,text="ENTER ITEM CODE",font=("AgencyFB","12","bold"),bg="#66FF66")
    l1.grid(row=0,column=0)
    e1=Entry(top,textvariable=code1)
    e1.grid(row=0,column=1)
    b1=Button(top,text=" SEARCH ",command=tksearch,font=("AgencyFB","10","bold"),bg="#00CCFF")
    b1.grid(row=1,column=1)

def invoice_history():
    h=P.invoicehist()
    top_hist=Toplevel()
    top_hist.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    tv=Treeview(top_hist,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="30")
    tv.grid(row=1,column=0)
    tv.column(1,width=100)
    tv.column(2,width=100)
    tv.column(3,width=150)
    tv.column(4,width=100)
    tv.column(5,width=100)
    tv.column(6,width=100)
    tv.column(9,width=100)
    tv.heading(1,text="INVOICE NO")
    tv.heading(2,text="DATE")
    tv.heading(3,text="ITEM")
    tv.heading(4,text="PRICE")
    tv.heading(5,text="QUANTITY")
    tv.heading(6,text="TOTAL")
    tv.heading(7,text="MODE")
    tv.heading(8,text="CUSTOMER NAME")
    tv.heading(9,text="PHONE NO")
    for i in h:
        tv.insert("","end",values=i)
    
def admin1():
    global admin_top
    admin_top=Toplevel()
    admin_top.geometry("410x430")
    admin_top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    b1=Button(admin_top,text="         ADD STOCK         ",font=("AgencyFB","12","bold"),command=add_window,bg="#FFFFFF")
    b1.grid(row=0,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    b2=Button(admin_top,text="    DISPLAY STOCK     ",font=("AgencyFB","12","bold"),command=display_window,bg="#FF66FF")
    b2.grid(row=1,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    b3=Button(admin_top,text="    SEARCH STOCK    ",font=("AgencyFB","12","bold"),command=search_window,bg="#9999FF")
    b3.grid(row=2,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    b4=Button(admin_top,text="      UPDATE NAME      ",font=("AgencyFB","12","bold"),command=updatename_window,bg="#00FF00")
    b4.grid(row=3,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    b4=Button(admin_top,text="  UPDATE QUANTITY  ",font=("AgencyFB","12","bold"),command=updatequantity_window,bg="#FFFF00")
    b4.grid(row=4,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    b4=Button(admin_top,text="      UPDATE PRICE      ",font=("AgencyFB","12","bold"),command=updateprice_window,bg="#FF7F00")
    b4.grid(row=5,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    b5=Button(admin_top,text="     DELETE STOCK     ",font=("AgencyFB","12","bold"),command=delete_window,bg="#FF0000")
    b5.grid(row=6,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    b5=Button(admin_top,text="PURCHASE HISTORY",font=("AgencyFB","12","bold"),command=invoice_history,bg="#00FFFF")
    b5.grid(row=7,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
    

def customer():
    c.add_to_cart()

def login():
    global toplog
    unm1=unm.get()
    pwd1=pwd.get()
    if unm1=="admin" and pwd1=="1234":
        t1.delete(0,END)
        t2.delete(0,END)
        toplog.destroy()
        admin1()
    else:
        messagebox.showerror("Error","Invalid Username or Password")
        t1.delete(0,END)
        t2.delete(0,END)
        t1.focus_set()   
        
def adm_login():
    global toplog
    global t1
    global t2
    toplog=Toplevel()
    toplog.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    toplog.geometry("350x200")
    label1=Label(toplog,text="LOGIN PAGE",font=("AgencyFB","14","bold"),bg="#FF99FF")
    label1.grid(row=1,column=2)
    l1=Label(toplog,text="USERNAME",font=("AgencyFB","12","bold"),bg="#66FF66")
    l1.grid(row=3,column=1)
    t1=Entry(toplog,textvariable=unm,width=25)
    t1.grid(row=3,column=2)
    l2=Label(toplog,text="PASSWORD",font=("AgencyFB","12","bold"),bg="#66FF66")
    l2.grid(row=5,column=1)
    t2=Entry(toplog,textvariable=pwd,show='*',width=25)
    t2.grid(row=5,column=2)
    b1=Button(toplog,text="LOGIN",command=login,font=("AgencyFB","12","bold"),bg="#00C9FF")
    b1.grid(row=7,column=2)

btn1_main=Button(root,text="     ADMIN     ",command=adm_login,bg="#FFE002",font=("AgencyFB","12","bold"))
btn1_main.grid(row=0,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
btn2_main=Button(root,text="CUSTOMER",command=customer,bg="#36FF00",font=("AgencyFB","12","bold"))
btn2_main.grid(row=1,column=1,columnspan=1,pady=10,padx=10,ipadx=100)
root.mainloop()