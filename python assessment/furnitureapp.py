from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_new"
        )

def insert_data():
    if e_id.get()=="" or e_prod_name.get()=="" or e_prod_price.get()=="" or e_prod_quantity.get()=="":
        msg.showinfo("Insert status","All Fields are mandatory")

    else:
        conn=create_conn()
        cursor=conn.cursor()

        query="insert into furniture_shop(id,prod_name,prod_price,prod_quantity) values (%s,%s,%s,%s)"
        args=(e_id.get(),e_prod_name.get(),e_prod_price.get(),e_prod_quantity.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_id.delete(0,'end')
        e_prod_name.delete(0,'end')
        e_prod_price.delete(0,'end')
        e_prod_quantity.delete(0,'end')
        
        msg.showinfo("Insert status","Your data is Inserted")

def search_data():
    
    e_prod_name.delete(0,'end')
    e_prod_price.delete(0,'end')
    e_prod_quantity.delete(0,'end')

    if e_id.get()=="":
         msg.showinfo("Search status","Id is mandatory")

    else:
        
        
        conn=create_conn()
        cursor=conn.cursor()

        query="select * from furniture_shop where id=%s"

        args=(e_id.get(),)
        cursor.execute(query,args)

        row=cursor.fetchall()
        
        if row:
            e_prod_name.insert(0,row[0][1])
            e_prod_price.insert(0,row[0][2])
            e_prod_quantity.insert(0,row[0][3])
 
        else:
            msg.showinfo("Search status","Id is not found")
            conn.close()

def delete_data():

    if e_id.get()=="":
         msg.showinfo("delete status","Id is mandatory")

    else:
        
        
        conn=create_conn()
        cursor=conn.cursor()

        query="delete from furniture_shop where id=%s"

        args=(e_id.get(),)
        cursor.execute(query,args)

        conn.commit()
        conn.close()
        e_id.delete(0,'end')

        msg.showinfo("delete status","Data delete successfully")

        
def update_data():

    if e_id.get()=="" or e_prod_name.get()=="" or e_prod_price.get()=="" or e_prod_quantity.get()=="":
        msg.showinfo("Update status","All fields are mandatory")

    else:
        conn=create_conn()
        cursor=conn.cursor()

        query="UPDATE furniture_shop SET prod_name = %s, prod_price = %s, prod_quantity = %s WHERE id = %s"

        args=(e_prod_name.get(), e_prod_price.get(), e_prod_quantity.get(), e_id.get())
        cursor.execute(query,args)
        
        
        conn.commit()
        conn.close()
        
        e_id.delete(0,'end')
        e_prod_name.delete(0,'end')
        e_prod_price.delete(0,'end')
        e_prod_quantity.delete(0,'end')

        msg.showinfo("update status","Data update successfully")
        
def total_price():
    if e_id.get()=="" or e_prod_name.get()=="" or e_prod_price.get()=="" or e_prod_quantity.get()=="":
        msg.showinfo("total price","All fields are mandatory")

    else:
        conn=create_conn()
        cursor=conn.cursor()
        
        price= float(e_prod_price.get())
        quantity=int(e_prod_quantity.get())

        total=price * quantity
        l_total=Label(root,text="")
        l_total.place(x=400,y=300)

        l_total.config(text=f"Total price : {total:.2f}")

        e_id.delete(0,'end')
        e_prod_name.delete(0,'end')
        e_prod_price.delete(0,'end')
        e_prod_quantity.delete(0,'end')
        
            

        

root=Tk()
root.geometry("550x400")
root.title("My furniture app")
root.resizable(width=False,height=False)

l_info=Label(root,text="id info")
l_info.place(x=400,y=100)

l_info=Label(root,text="chair - 1")
l_info.place(x=400,y=150)

l_info=Label(root,text="Table - 2")
l_info.place(x=400,y=200)

l_info=Label(root,text="Sofa - 3")
l_info.place(x=400,y=250)

l_id=Label(root,text="ID")
l_id.place(x=50,y=100)

l_prod_name=Label(root,text="Product Name")
l_prod_name.place(x=50,y=150)

l_prod_price=Label(root,text="Product Price")
l_prod_price.place(x=50,y=200)

l_prod_quantity=Label(root,text="Product Quantity")
l_prod_quantity.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=100)

e_prod_name=Entry(root)
e_prod_name.place(x=150,y=150)

e_prod_price=Entry(root)
e_prod_price.place(x=150,y=200)

e_prod_quantity=Entry(root)
e_prod_quantity.place(x=150,y=250)

insert=Button(root,text="Insert",bg="black",fg="white",font=("Arial",13),command=insert_data)
insert.place(x=35,y=300)

insert=Button(root,text="Search",bg="black",fg="white",font=("Arial",13),command=search_data)
insert.place(x=90,y=300)

insert=Button(root,text="Delete",bg="black",fg="white",font=("Arial",13), command=delete_data)
insert.place(x=155,y=300)

insert=Button(root,text="Update",bg="black",fg="white",font=("Arial",13),command=update_data)
insert.place(x=210,y=300)

insert=Button(root,text="Total",bg="black",fg="white",font=("Arial",13),command=total_price)
insert.place(x=275,y=300)

root.mainloop()




