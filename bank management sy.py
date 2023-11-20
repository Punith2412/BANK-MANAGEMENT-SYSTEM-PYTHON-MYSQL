import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passward='punith@037103033',database='bms')

def open_account():
    name=input("enter your name:")
    acc=input("enter your acc no:")
    dob=input("enter your dob:")
    add=input("enter your address:")
    con=input("enter your contact:")
    op_bal=int(input("enter your opening balance:"))

    data1=(name,acc,dob,add,con,op_bal)
    data2=(name,acc,op_bal)

    sql1=('insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=mydb.cursor()

    x.execute(sql1,data1)
    x.execute(sql2,data2)

    mydb.commite()
    print("data entered successfully")
    main()

def depost():
     amount=input("enter the amount to deposit:")
     acc=input("enter your acc no:")
     a="select balance from amount where acc_no=%s"
     data1=(acc,)
     x=mydb.cursor()
     x.execute(a,data1)
     result=x.fetchone()
     t=result[0]+amount
     sql=('update amount set balance where acc_no=%s')
     d=(t,acc)
     x.execute(sql,d)
     mydb.commit()
     print("___________________")
     main()

def withdrawn():
    amount=input("enter the amount to withdrawn:")
    acc=input("enter your acc no:")
    a="select balance from amount where acc_no=%s"
    data1=(acc,)
    x=mydb.cursor()
    x.execute(a,data1)
    result=x.fetchone()
    t=result[0]-amount
    sql=('update amount set balance where acc_no=%s')
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    print("______________________________")
    main()

def balance():
    acc=input("enter your acc no:")
    a="select*from amount where acc_no=%s"
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    mydb.commit()


def main():
    print("""
          1.open new account
          2.deposit amount
          3.withdrawn amount
          4.balance enquery
          5.show customer details
          6.close an account
          """)
    choose=int(input("choose your option:"))
    if(c==1):
        open()
        print("1.open new account")
            
    elif(c==2):
        deposit()
        print("2.deposit amount")
    
    elif(c==3):
        withdrawn()
        print("3.withdrawn amount")
        
    elif(c==4):
        balance()
        print("4.balance enquery")
        
    elif(c==5):
        customer+detail()
        print("5.show customer detail")

    elif(c==6):
        print("6.close an account")
    
    else:
        print("enter the valid number")
        main()
       
main()
    
    

     
     
    
