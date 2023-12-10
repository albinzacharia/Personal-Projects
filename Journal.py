#Zjournal
import os.path
from getpass import getpass
print('Z_JOURNAL')
while True:
    ch=int(input(' 1.Write \n 2.Read \n 3.Update log \n 4.Delete log \n 5.Exit \n Enter your choice: '))
    if ch==1:
        a=input("Enter day and date : ")
        save_path='savepath’
        txd='dates.txt'
        paths=os.path.join(save_path,txd)
        filed=open(paths,'a+')
        filed.write(a)
        filed.write('\n')
        filed.close()
        tx=a+'.txt'
        save_path='savepath’
        paths=os.path.join(save_path,tx)
        file=open(paths,'w+')
        while True:
            wrt=input("Log: ")
            if "//" in wrt:
                file.write(wrt)
                file.close()
                break
            else:
                print('Please use "//" at the end to save your log!')
                continue
            
    elif ch==2:
        psw=getpass("Enter the password hehehe : ")
        if psw=='******':           
            save_path='savepath’'
            rd='dates.txt'
            paths=os.path.join(save_path,rd)
            try:
                filed=open(paths,'r+')
                reaad=filed.read()
                print(reaad)
                filed.close()
            except OSError:
                print('File not found')
                continue
            b=input("Which log do you want to read? : ")
            txx=b+'.txt'
            save_path='savepath’
            paths=os.path.join(save_path,txx)
            try:
                filex=open(paths,'r+')
                reed=filex.read()
                print(reed)
                filex.close()
            except OSError:
                print('File not found')
                continue
        else:
            print('Wrong password vro')
            continue

    elif ch==3:
        psw=getpass("Enter the password hehehe : ")
        if psw=='******’:           
            c=input("Enter Log you wish to update : ")
            txa=c+'.txt'
            save_path='savepath’
            paths=os.path.join(save_path,txa)
            while True:
                filea=open(paths,'r+')
                r=filea.read()
                print(r)
                apnd=input(" ")
                if "///" in apnd:
                    filea.write(apnd)
                    filea.close()
                    break
                else:
                    print('Please use "///" at the end to save your log!')
                    continue
    elif ch==4:
        psw=getpass("Enter the password hehehe : ")
        if psw=='******i':
            d=input("Enter log which you wish to delete : ")
            print("Are you sure you want to delete ",d,"? (Y/N)")
            conf=input(" ")
            if conf=='Y' or conf=='y':
                txd=d+'.txt'
                save_path='savepath’
                paths=os.path.join(save_path,txd)
                os.remove(paths)
            else:
                continue
        else:
            print('Wrong password vro')
            continue

    elif ch==5:
        break
    else:
        print('Enter a valid choice smh')
        continue
