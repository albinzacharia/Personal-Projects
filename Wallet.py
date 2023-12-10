#wallet
import mysql.connector
mycon=mysql.connector.connect (host='localhost', user='root', passwd='orin360', database='wallet')
cursor=mycon.cursor()
cursor.execute('select * from wallet')
print("My Wallet")
crnt=cursor.fetchone()
c=int(''.join(map(str,crnt)))
while True:
    a=input("To show current savings, press 1 \n To add money, press 2 \n To take money, press 3 \n To exit, press 4 \n Enter your choice: ")
    if a=='1':
        print(c)
        continue
    elif a=='2':
        rcvd=int(input("Enter the money recieved : "))
        ad=rcvd+c
        print(ad)
        upadd="update wallet set Money={}".format(ad)
        cursor.execute(upadd)
        mycon.commit()
        continue
    elif a=='3':
        gne=int(input("Enter the money spent : "))
        sub=c-gne
        print(sub)
        upsub="update wallet set Money={}".format(sub)
        cursor.execute(upsub)
        mycon.commit()
        continue
    else:
        break
mycon.close()
