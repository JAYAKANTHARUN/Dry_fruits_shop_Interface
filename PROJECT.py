import pymysql

db=pymysql.connect(host="localhost",user="root",passwd="root",database="dryfruitshop")
c=db.cursor()
    
def add(L):
    code=L[0]
    name=L[1]
    price=L[2]
    quantity=L[3]
    q="insert into stock values({},'{}',{},{})".format(code,name,price,quantity)
    c.execute(q)
    db.commit()

def display():
    l=[]
    c.execute("select * from stock")
    data=c.fetchall()
    for i in data:
        l.append(list(i))
    return l
    db.commit()    
    
def search(L):
    code=L[0]
    l=[]
    q="select * from stock where item_code={}".format(code)
    c.execute(q)
    data=c.fetchall()
    for i in data:
        l.append(list(i))
    return l    
    db.commit()
    
def delete(L):
    code=L[0]
    c.execute("delete from stock where item_code={}".format(code))
    db.commit()
    
def updatename(L):
    code=L[0]
    itemname=L[1]
    q="update stock set item='{}' where item_code={}".format(itemname,code)
    c.execute(q)
    db.commit()
    
def updateprice(L):
    code=L[0]
    price=L[1]
    c.execute("update stock set price_per_kg={} where item_code={}".format(price,code))
    db.commit()
    
def updatequantity(L):
    code=L[0]
    quantity=L[1]
    q="update stock set quantity_in_kg=quantity_in_kg+{} where item_code={}".format(quantity,code)
    c.execute(q)
    db.commit()

def search_item():
    l3=["Select"]
    q="select item from stock"
    c.execute(q)
    data=c.fetchall()
    for row in data:
        l3.append(row[0])
    return l3

def search_price(item):
    l3=[]
    q="select * from stock where item='{}'".format(item)
    c.execute(q)
    data=c.fetchall()
    for row in data:
        l3.append(list(row))
    return l3   

def invoicehist():
    l=[]
    c.execute("select invoiceno,indate,item,price,qty,total,mode,custname,phone from invoice")
    data=c.fetchall()
    for i in data:
        l.append(list(i))
    return l
    db.commit()