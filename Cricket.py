import random
def batting():
        global j
        j=0
        print("BATTING")
        while True:           
            br=int(input("Enter runs (1-6) : "))
            if br>6:
                print("Enter runs between (1-6): \n")
                continue
            else:
                print(br)
                print("Computer chose: \n")
                blr=(random.randint(1,6))
                print(blr)
                if blr==br:
                    print("\nOUT!")
                    print("\nTotal Runs: ",j)
                    break
                else:
                    j=j+br
                    continue
             

def balling():
        global i
        i=0
        print("BALLING")
        while True:
            blr=int(input("Enter runs (1-6) : "))
            if blr>6:
                print("Enter runs between (1-6): \n")
                continue
            else:          
                print(blr)
                print("Computer chose: \n")
                br=(random.randint(1,6))
                print(br)
                if blr==br:
                    print("\nOUT!")
                    print("\nTotal Runs: ",i)
                    break
                else:
                    i=i+br
                    continue
            

while True:
    e=2 
    o=1
    ch=int(input("ODD (1) or EVEN (2) ? \n Enter choice: "))
    if ch==1:
        comp=e
    elif ch==2:
        comp=o
    else:
        print("Enter 1 for Odd or 2 for Even: \n")
        continue
    toss=int(input("Enter the number (0 to 9): "))
    if toss>9:
        print("Enter between 0 and 9: \n")
        continue
    else:
        tosscomp=random.randint(0,9)
        sumtoss=toss+tosscomp
        compresult=tosscomp%2
        tossresult=sumtoss%2
        if tossresult==0:
            print("Toss won for Even!")
        else:
            print("Toss won for Odd!")
        if tossresult==compresult:
            print("Computer gets to choose (Bat or Ball): \n")
            compchoose=(random.randint(1,2))
            if compchoose==1:
                print("Computer chooses to bat! ")
                balling()
                batting()
                print("||Total Runs after match||\n You: ",j,"\n Computer: ",i)
                if j>i:
                    print("\nYou won!")
                    break
                else:
                    print("\nYou lost")

            else:
                print("Computer chooses to ball! ")
                batting()
                balling()
                print("||Total Runs after match||\n You: ",j,"\n Computer: ",i)
                if j>i:
                    print("\nYou won!")
                    break
                else:
                    print("\nYou lost")
        else:
            tosschoice=int(input("You get to choose (Bat (1) or Ball(2)): \n"))
            if(tosschoice==1):
                print("You chose to bat! ")
                batting()
                balling()
                print("||Total Runs after match||\n You: ",j,"\n Computer: ",i)
                if j>i:
                    print("\nYou won!")
                    break
                else:
                    print("\nYou lost")

            elif(tosschoice==2):
                print("You chose to ball! ") 
                balling()
                batting()
                print("||Total Runs after match||\n You: ",j,"\n Computer: ",i)
                if j>i:
                    print("\nYou won!")
                    break
                else:
                    print("\nYou lost")
            else:
                print("Choose 1 or 2 for Bat or Ball: \n")
                continue
        break
