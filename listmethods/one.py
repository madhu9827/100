l=[]
n=int(input("enter list length:"))
for i in range(n):
    a=int(input("enter a number:"))
    l.append(a)
print(l)
while True:
    options=["Options","1.insert ","2.delete ","3.sort ","4.reverse ","5.exit "]
    for i in options:
        print(i)
    one=int(input("enter a option to execute:"))
    if one==1:
        val=int(input("enter a value to insert:"))
        l.append(val)
        print("New list=",l)
    elif one==2:
        ac=int(input("enter a value to delete:"))
        if ac in l:
            l.remove(ac)
            print(l)
        else:
            print("not a vaid number")
    elif one==3:
        l.sort()
        print(l)
    elif one==4:
        l.reverse()
        print(l)
    elif one==5:
        print("exiting the program")
        break 
    else:
        print("cannot in option")