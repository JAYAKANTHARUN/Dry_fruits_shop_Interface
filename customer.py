from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import date
import pymysql
import PROJECT as p

db=pymysql.connect(host="localhost",user="root",passwd="root",database="dryfruitshop")
c1=db.cursor()
        
def add_to_cart():
    root=Toplevel()
    root.geometry("1000x600")
    root.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
    iprice = StringVar()
    cname = StringVar()
    cadd = StringVar()
    cph = StringVar()
    pmode = StringVar()
    nob = StringVar()
    acno = StringVar()
    ifsc = StringVar()

    def select_item(event):
        global lst1
        c1=combobox1.get()
        lst1=p.search_price(c1)
        iprice.set(lst1[0][2])
    def select_item1(event):
        c_pay=combobox_pay.get()
        if combobox_pay.current() == 1:
            btn_pay=Button(top_pay,text="OK",command=invoice_generate)
            btn_pay.place(x=100,y=140)       
    sl=[]
    def addbill():
        inm=combobox1.get()
        p=iprice.get()
        qty=q.get()
        q1=lst1[0][3]
        if float(qty)<=q1:
            tot=float(qty)*float(p)
            l=[inm,p,qty,tot]
            sl.append(l)
            parts_list.insert(END,l)
            t2.delete(0,END)
            t3.delete(0,END)
        else:
            messagebox.showerror("Stock Unavailable","Available Quantity : "+str(q1))
            t2.delete(0,END)
            t3.delete(0,END)
            
        

    def rem_item():
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        parts_list.delete(index)
        del sl[index]

    def get_invoiceno():    
        
        l3=[]
        q="select max(invoiceno) from invoice"
        c1.execute(q)
        data=c1.fetchall()
        a=data[0][0]
        if a!= None:
            invoiceno = a+1
        else:
            invoiceno = 1000
        return invoiceno

    def pay():
        global combobox_pay
        global top_pay
        top_pay=Toplevel()
        top_pay.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
        top_pay.geometry("700x600")
        lab_pay1 = Label(top_pay, text='CUSTOMER NAME', font=('bold', 11))
        lab_pay1.place(x=20,y=20)
        entry_pay1 = Entry(top_pay, textvariable=cname)
        entry_pay1.place(x=200,y=20)
        lab_pay2 = Label(top_pay, text='CUSTOMER ADDRESS', font=('bold', 11))
        lab_pay2.place(x=20,y=50)
        entry_pay2 = Entry(top_pay, textvariable=cadd)
        entry_pay2.place(x=200,y=50)
        lab_pay3 = Label(top_pay, text='CONTACT NO.', font=('bold', 11))
        lab_pay3.place(x=20,y=80)
        entry_pay3 = Entry(top_pay, textvariable=cph)
        entry_pay3.place(x=202,y=80)
        lab_pay4 = Label(top_pay, text='MODE OF PAYMENT', font=('bold', 11))
        lab_pay4.place(x=20,y=110)
        combobox_pay=Combobox(top_pay)
        items=("SELECT","CASH ON DELIVERY")
        combobox_pay["values"]=items
        combobox_pay.place(x=200,y=110)
        combobox_pay.current(0)
        combobox_pay.bind("<<ComboboxSelected>>",select_item1)
        
    def invoice():
        global ino
        global top
        top=Toplevel()
        top.iconbitmap(r"D:\dry_fruits_shop_interface\shopping_cart.ico")
        ino=get_invoiceno()
        lbl=Label(top,text="3JN ONLINE DRY FRUIT SHOP")
        lbl.pack()
        d1=str(date.today())
        lb2=Label(top,text="DATE : "+d1)
        lb2.pack()
        lb2=Label(top,text="INVOICE NO : "+str(ino))
        lb2.pack()
        tv=Treeview(top,columns=(1,2,3,4),show="headings",height="11")
        tv.pack()
        tv.heading(1,text="ITEM NAME")
        tv.heading(2,text="ITEM PRICE")
        tv.heading(3,text="QUANTITY")
        tv.heading(4,text="TOTAL")
        t=0
        for row in sl:
            t=t+row[3]
            tv.insert("","end",values=row)
        l=["","","Total : ",t]
        tv.insert("","end",values=l)
        btn1= Button(top,text="PROCEED TO PAY",command=pay)
        btn1.pack()
        btn=Button(top,text="CLOSE",command=top.destroy)
        btn.pack()
    
    def invoice_generate():
        parts_list.delete(0,END)
        date1=date.today()
        print(ino,date1,sl)
        cnm=cname.get()
        cad=cadd.get()
        cp=cph.get()
        md=combobox_pay.get()
        for i in sl:
            item=i[0]
            price=i[1]
            qty=i[2]
            total=i[3]
            q="insert into invoice values({},'{}','{}',{},{},{},'{}','{}','{}','{}')".format(ino,date1,item,price,qty,total,md,cnm,cad,cp)
            c1.execute(q)
            db.commit()
            q1="update stock set quantity_in_kg=quantity_in_kg-{} where item='{}'".format(qty,item)
            c1.execute(q1)
            db.commit()
        messagebox.showinfo(" DRY FRUIT SHOP ","YOUR ORDER HAS BEEN PLACED, THANK YOU FOR SHOPPING WITH US, FOR MORE DETAILS CONTACT :- 1234567890")
        top_pay.destroy()
        top.destroy()
        root.destroy()  

    l3=[]
    q="select item,price_per_kg from stock"
    c1.execute(q)
    data=c1.fetchall()
    for row in data:
        l3.append(list(row))
    tv=Treeview(root,columns=(1,2),show="headings",height="20")
    tv.place(x=20,y=20)
    tv.column(1,width=100)
    tv.column(2,width=100)
    tv.heading(1,text="ITEM NAME")
    tv.heading(2,text="PRICE/KG")
    t=0
    for row in l3:
        tv.insert("","end",values=row)
    
    cl1=Label(root,text='ITEM NAME')
    cl1.place(x=250,y=20)
    combobox1=Combobox(root)
    item=p.search_item()
    items=tuple(item)
    combobox1["values"]=items
    combobox1.place(x=350,y=20)
    combobox1.current(0)
    combobox1.bind("<<ComboboxSelected>>",select_item)

    q = StringVar()

    l2 = Label(root, text='PRICE')
    l2.place(x=250,y=50)
    t2 = Entry(root, textvariable=iprice)
    t2.place(x=350,y=50)

    l3 = Label(root, text='QUANTITY')
    l3.place(x=250,y=80)
    t3 = Entry(root, textvariable=q)
    t3.place(x=350,y=80)


    b1=Button(root,text="ADD TO STOCK",command=addbill)
    b1.place(x=330,y=110)

    parts_list = Listbox(root, height=8, width=50, border=0)
    parts_list.place(x=250,y=140)

    b2=Button(root,text="CLOSE",command=root.destroy)
    b2.place(x=250,y=300)
    
    b2=Button(root,text="REMOVE",command=rem_item)
    b2.place(x=350,y=300)

    b3=Button(root,text="GENERATE BILL",command=invoice)
    b3.place(x=450,y=300)