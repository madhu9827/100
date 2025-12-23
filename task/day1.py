nums = [1, 2, 3, 1, 1, 3] 
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            count=count+1
print(count)



# 2nd problem
nums = [1, 1, 1] 
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            count=count+1
print(count)

# 
# candies = [2, 3, 5, 1, 3] 
# extraCandies = 3 
# max=max(candies)
# cand=[]
# for i in candies:
#     if (i+extraCandies)>=max:
#         cand.append(True)
#     else:
#         cand.append(False)
# print(cand)


candi=[4, 2, 1, 1, 2] 
extraCandies = 1
ma=max(candi) 
can=[]
for i in candi:
    if(i+extraCandies)>=ma:
        can.append(True)
    else:
        can.append(False)
print(can)