def arr():
   num=int(input("enter the no of customers: "))
   cart=[]
   for i in range(1,num+1):
      customer=[]
      while (True):
         items=int(input(f"enter the cart items of {i} customer: "))
         if items==0:
            break
         (customer.append(items))
      cart.append(customer)
   totals = []
   for customer in cart:
      totals.append(sum(customer))
   return totals
   # for total in totals: 
   #    if total >= 5000:
   #       return (total-(total/100)*20)
   #    elif total > 1000:
   #       return (total-(total/100)*15)
   #    elif total > 500:
   #       return (total-(total/100)*10)
   #    else:
   #       return totals
print(arr())