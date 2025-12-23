n=[[100,400,127],
   [450,600],
   [127,128,57,600],
   [0,1,3],[2500,2500]]
l=[]
for i in n:
    total=sum(i)
    print(total)
    if total >0 and total <500:
        discount=total*0.05
        final=total-discount
        l.append(final)
    elif total >500 and total<1000:
        discount1=total*0.05
        final=total-discount1
        l.append(final)
    elif total>1000 and total<5000:
        discount2=total*0.15
        final=total-discount2
        l.append(final)
    elif total>=5000:
        discount3=total*0.20
        final=total-discount3
        l.append(final)
    else:
        print("nothing")
print(l)

def y(total,dis):
        dis=total*(dis/100)
        final=total-dis
        return final
print(y(627,5))
print(y(1050,15))


    
    


