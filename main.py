import random
from mysql.connector import(connection)
cnt=connection.MySQLConnection(user='root',password='Nivi@2005',host='127.0.0.1',database='gmms')
if cnt.is_connected()==False:
    print("Not connected ")
else:
    print("Connected to GROCERY  , WELCOME ")
cur=cnt.cursor()
print('create a admin - enter 0')
print('enter stock details - enter 1')
print('create a user account - enter 2')
print('to view stock details - enter 3')
print("to purchase items - enter 4")
print('to confirm delivery - enter 5')
print("to take delivery - enter 6")
ch=int(input())
if ch==0:
    print('Please enter the store password ')
    a=input()
    if a=="Nivethaa":
        print('enter your id')
        id=int(input())
        print('enter your name')
        n=input()
        print('enter your phoneno')
        p=input()
        s="insert into admindata (id,name,phoneno) values (%s,%s,%s);"
        t=(id,n,p)
        try:
            cur.execute(s,t)
            cnt.commit()
        except Exception as e:
            print(e)
    else:
        print('Fake id')
elif ch==1:
    print('to enter vegetable details-vegetable , to enter fruit details-fruit')
    k=input()
    if k=="vegetable":
        print('enter your staff id')
        sid=int(input())
        b="SELECT id FROM gmms.admindata;"
        r=[]
        try:
            cur.execute(b)
            r=cur.fetchall()
        except Exception as e:
            print(e)
      
        flag=0
        for i in r:
           for j in i:
            if sid==j:
                flag=1
        if flag==1:
            print("enter the vegeid")
            vid=int(input())
            print('enter the vegename')
            vname=input()
            print('enter the vegeqty')
            vqty=int(input())
            print('enter the vegeup')
            vup=int(input())
            s="insert into vegeinfo (vegeid,vegename,vegeqyt,vegeup) values (%s,%s,%s,%s);"
            t=(vid,vname,vqty,vup)
            try:
                cur.execute(s,t)
                cnt.commit()
            except Exception as e:
                print(e)
        else:
            print('you are not a staff')
    elif k=="fruit":
        print('enter your staff id')
        sid=int(input())
        b="SELECT id FROM gmms.admindata;"
        r=[]
        try:
            cur.execute(b)
            r=cur.fetchall()
        except Exception as e:
            print(e)
      
        flag=0
        for i in r:
           for j in i:
            if sid==j:
                flag=1
        if flag==1:
            print("enter the fruid")
            fid=int(input())
            print('enter the fruname')
            fname=input()
            print('enter the fruqty')
            fqty=int(input())
            print('enter the fruup')
            fup=int(input())
            s="insert into fruinfo (fruid,fruname,fruqty,fruup) values (%s,%s,%s,%s);"
            t=(fid,fname,fqty,fup)
            try:
                cur.execute(s,t)
                cnt.commit()
            except Exception as e:
                print(e)
        else:
            print('you are not a staff')
elif ch==2:
        print('to get your customer id dial 999 - enter your id')
        id=int(input())
        print('enter your name')
        n=input()
        print('enter your phoneno')
        p=input()
        s="insert into cusinfo (cusid,cusname,cusphoneno) values (%s,%s,%s);"
        t=(id,n,p)
        try:
            cur.execute(s,t)
            cnt.commit()
        except Exception as e:
             print(e)
elif ch==3:
    print('to see vegetable details type vegetable,to fruit details type fruit')
    c=input()
    if(c=="vegetable"):
        s="SELECT vegeid,vegename,vegeqyt,vegeup FROM vegeinfo;"
        r=[]
        try:
            cur.execute(s)
            r=cur.fetchall()
        except Exception as e:
                print(e)
        print("V.ID | V.NAME | V.QTY | V.UNIT/PRICE ")
        for i in r:
            print(i)
    elif(c=="fruit"):
        s="SELECT fruid,fruname,fruqty,fruup FROM fruinfo;"
        r=[]
        try:
            cur.execute(s)
            r=cur.fetchall()
        except Exception as e:
                print(e)
        print("F.ID | F.NAME | F.QTY | F.UNIT/PRICE ")
        for i in r:
            print(i)
elif ch==4:
    print('To start purchase - enter 1')
    k = int(input())
    res = []

    while k == 1:
        print('\nTo purchase fruit enter - 1, to purchase vegetable enter - 2, to close purchase enter - 3')
        t = int(input())
    
        if t == 1:
            s = "SELECT fruid, fruname, fruqty, fruup FROM fruinfo;"
            r = []
            try:
                cur.execute(s)
                r = cur.fetchall()
            except Exception as e:
                print("Error fetching fruit data:", e)
                continue
        
            print("\nF.ID | F.NAME | F.QTY | F.UNIT/PRICE")
            for i in r:
                print(i)
        
            try:
                n = int(input("Enter the fruit ID you need: "))
                m = int(input("Enter quantity: "))
            
                cur.execute("SELECT fruname, fruqty, fruup FROM fruinfo WHERE fruid = %s;", (n,))
                fruit = cur.fetchone()
                if fruit:
                    fname, available_qty, unit_price = fruit
                    if m > available_qty:
                        print("Insufficient quantity available.")
                        continue
                
                    total_price = m * unit_price
                    new_qty = available_qty - m
                    cur.execute("UPDATE fruinfo SET fruqty = %s WHERE fruid = %s;", (new_qty, n))
                    cnt.commit()

                    res.append([n, fname, m, total_price])
                    print(f"Added to bill: {fname} x {m} = {total_price}")
                else:
                    print("Fruit ID not found.")
            except Exception as e:
                print("Error processing fruit purchase:", e)
                continue

        elif t == 2:
            s = "SELECT vegeid, vegename, vegeqyt, vegeup FROM vegeinfo;"
            r = []
            try:
                cur.execute(s)
                r = cur.fetchall()
            except Exception as e:
                print("Error fetching vegetable data:", e)
                continue
        
            print("\nV.ID | V.NAME | V.QTY | V.UNIT/PRICE")
            for i in r:
                print(i)
        
            try:
                n = int(input("Enter the vegetable ID you need: "))
                m = int(input("Enter quantity: "))
            
                cur.execute("SELECT vegename, vegeqyt, vegeup FROM vegeinfo WHERE vegeid = %s;", (n,))
                veg = cur.fetchone()
                if veg:
                    vname, available_qty, unit_price = veg
                    if m > available_qty:
                        print("Insufficient quantity available.")
                        continue
                
                    total_price = m * unit_price
                    new_qty = available_qty - m
                    cur.execute("UPDATE vegeinfo SET vegeqyt = %s WHERE vegeid = %s;", (new_qty, n))
                    cnt.commit()

                    res.append([n, vname, m, total_price])
                    print(f"Added to bill: {vname} x {m} = {total_price}")
                else:
                    print("Vegetable ID not found.")
            except Exception as e:
                print("Error processing vegetable purchase:", e)
                continue

        elif t == 3:
            print("Closing purchase.\n")
            break
        else:
            print("Invalid input. Try again.")

# Final Purchase Summary
    print("\nFinal Purchase Summary:")
    print("ID | NAME | QTY | PRICE")
    for item in res:
        print(item)

# Confirm and Save
    confirm = int(input("\nTo confirm and save bill enter 1, to cancel enter 0: "))

    if confirm == 1:
        try:
        # Separate out ID, Name, QTY, and Total Price
            vfid = ','.join(str(item[0]) for item in res)
            vfname = ','.join(str(item[1]) for item in res)
            vfqty = ','.join(str(item[2]) for item in res)
            vfprice = sum(item[3] for item in res)

            cur.execute(
                "INSERT INTO billinfo (vfid, vfname, vfqty, vfprice) VALUES (%s, %s, %s, %s)",
                (vfid, vfname, vfqty, vfprice)
            )
            cnt.commit()
            print("Bill saved successfully to database.")
        except Exception as e:
            print("Error saving bill:", e)
    else:
        print("Bill was not saved.")
elif ch==5:
        print("See the below bill details and confirm with your bill id")
        s="SELECT billid,vfid,vfname,vfqty,vfprice FROM billinfo;"
        r=[]
        try:
            cur.execute(s)
            r=cur.fetchall()
        except Exception as e:
                print(e)
        print("B.ID | VF.ID | VF.NAME | VF.QTY | VF.PRICE ")
        for i in r:
            print(i)
        h=int(input("Enter a bill id:"))
        i=input("Enter a Phone No:")
        c=input("Enter a Name:")
        l=input("Enter a Address:")
        d="Not Delivered "
        e="Not Assigned "
        rd = random.randint(100, 999)
        f=(h,c,i,l,d,e,rd)
        rm="INSERT INTO deliinfo(billid,name,phoneno,address,status,delivname,otp) VALUES (%s,%s,%s,%s,%s,%s,%s);"
        try:
            cur.execute(rm,f)
            cnt.commit()
            print("Delivery Confirmed")
        except Exception as e:
            print(e)
        print("Please note your OTP")
        print(rd)
elif ch==6:
        print("to take delivery,enter your admin id")
        
        sid=int(input())
        b="SELECT id FROM gmms.admindata;"
        r=[]
        try:
            cur.execute(b)
            r=cur.fetchall()
        except Exception as e:
            print(e)
      
        flag=0
        for i in r:
           for j in i:
            if sid==j:
                flag=1
        if(flag==1):
            print("take billid which is not in status - Not Delivered")
            s="SELECT deliveryid,billid,name,phoneno,address,status,delivname FROM deliinfo;"
            r=[]
            try:
                cur.execute(s)
                r=cur.fetchall()
            except Exception as e:
                print(e)
            print("D.ID | B.ID | NAME | PHO.NO | ADD | STS | D.NAME ")
            for i in r:
                print(i)
            k=int(input())
            n="Delivered"
            j=input("Enter your name:")
            cur.execute("UPDATE deliinfo SET status = %s,delivname = %s WHERE billid = %s;", (n,j,k))
            cnt.commit()
            










        

    

    


        