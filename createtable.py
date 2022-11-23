import pymysql
def create_table():
    db=pymysql.connect(host="localhost",user="root",passwd="root",database="dryfruitshop")
    c=db.cursor()
    c.execute("create table stock(item_code integer primary key,item varchar(30),price_per_kg float,quantity_in_kg float)")
    c.execute("insert into stock values(101,'cashewnut',500,15)")
    c.execute("insert into stock values(102,'almond',300,18)")
    c.execute("insert into stock values(103,'apricot',250,10)")
    c.execute("insert into stock values(104,'dates',400,15)")
    c.execute("insert into stock values(105,'pista',800,10)")
    c.execute("insert into stock values(106,'walnut',1500,10)")
    c.execute("insert into stock values(107,'raisins',180,20)")
    c.execute("insert into stock values(108,'fig',700,8)")
    c.execute("insert into stock values(109,'peanut',100,20)")
    c.execute("insert into stock values(110,'hazelnut',2000,10)")
    db.commit()
    db.close()
create_table()