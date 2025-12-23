while True:
    n=["1.square","2.rectangle","3.circle","4.traingle","5.exit"]
    print(n)
    n=int(input("enter number:"))
    if n==1:
        print("for square")
        side=int(input("enter square:"))
        print("side of square",side*side)
    elif n==2:
        print("for rectangle")
        height=int(input("enter rectangle:"))
        length=int(input("enter a width of rectangle"))
        print("area of rectangle",height*length)
    elif n==3:
        print("for circle")
        r=int(input("enter a radius:"))
        print("area of circle",3.14*r*r)
    elif n==4:
        print("for traingle")
        height=int(input("enter a height of traingle:"))
        base=int(input("enter a base of traingle"))
        print("area of traingle",0.5*height*base)
    else:
        print("exit")