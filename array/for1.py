def append_items_price(User:int,size:int)->list:
    li = []
    print(f"_____________________Enter {User} user  items price : ______________________")
    for _ in range(size):
        li.append(int(input(f"Enter {_ + 1} Item price : ")))
    return li

def make_dis(total:int,dis:int)->float:
    temp_dis_value = total*(dis/100)
    return total - temp_dis_value

def log(li:list)->float:
    temp_sum = sum(li)
    if temp_sum >= 5000:
        final_total = make_dis(total=temp_sum,dis=20)
    elif temp_sum > 1000:
        final_total = make_dis(total=temp_sum,dis=15)
    elif temp_sum > 500:
        final_total = make_dis(total=temp_sum,dis=5)
    else:
        final_total = temp_sum
    return final_total
    

#start here
num_Users = int(input("Enter number of users : "))

items_size = []
for i in range(1,num_Users+1):
    temp = int(input(f"Enter the Cart items Size of User_{i} : "))
    items_size.append(temp)

total_users_cart_list = []
for user,size in enumerate(items_size):
    temp = append_items_price(User=user+1,size=size)
    total_users_cart_list.append(temp)

final_cart_after_discount = []

for user_cart in total_users_cart_list:
    temp = log(li=user_cart)
    final_cart_after_discount.append(temp)

print("____________________Total Bill Amount_______________________")
for user,total_price in enumerate(final_cart_after_discount):
    print(f"{user+1} User total price : {total_price} RS")

# print(final_cart_after_discount)