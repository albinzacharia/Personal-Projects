#passwd_manager
from getpass import getpass
import mysql.connector
mycon=mysql.connector.connect(host='localhost', user='rootusername', passwd='rootpassword', database='databasename')
c=mycon.cursor()
c.execute('select * from passwds')
sho=c.fetchall()
while True:
    passw=getpass(“Password: ")
    if passw=='**********':
        a=int(input("To show passwords Press 1 \n To store passwords Press 2 \n To quit Press 3 \n Enter your choice: "))
        if a==1:
            print(sho)
            continue
        elif a==2:
            b=input("Enter the Site name: ")
            print(b)
            d=input("Enter the password: ")
            print(d)
            c.execute('insert into passwds values (%s,%s)',(b,d))
            mycon.commit()
            continue
        elif a==3:
            break              
    else:
        print("Sorry")
        break




import os.path
from getpass import getpass
while True:
    ps=getpass('Password : ')
    if ps=='**********':
        while True:
            print('PASSWORD VAULT')
            print('\n 1.Store passwords \n 2.Show passwords \n 3.Exit')
            c=int(input('Enter your choice : '))
            if c==1:
                save_path='yoursavepath'
                v='vault.txt'
                paths=os.path.join(save_path,v)
                fs=open(paths,'a+')
                psw=input('Insert site name and password (use ":" to divide sitename and password) : ')
                fs.write(psw)
                fs.write('\n')
                fs.close()
                yn=input('Do you wish to continue? (Y/N): ')
                if yn=='Y' or yn=='y':
                    continue
                else:
                    break
            elif c==2:
                save_paths='yoursavepath'
                v='vault.txt'
                paths=os.path.join(save_paths,v)
                fr=open(paths,'r+')
                r=fr.read()
                print(r)
                fr.close()
                yn=input('Do you wish to continue? (Y/N): ')
                if yn=='Y' or yn=='y':
                    continue
                else:
                    break
            elif c==3:
                break
            else:
                print('Enter a valid choice!!')
                continue
        break
