 # day5th
# nums = [0, 1]
# n=len(nums)
# print(n) 

# nums = [0, 0, 1, 1]
# n1=nums.count(0)
# n2=nums.count(1)
# print(min(n1,n2)*2)

# nums = [1, 1, 0, 0, 1] 
# n1=nums.count(0)
# n2=nums.count(1)
# print(min(n1,n2)*2)
    

nums = [0, 1, 0]

count = 0
s = {}
max_value = 0

for i in range(len(nums)):
    if nums[i] == 0:
        count -= 1
    else:
        count += 1

    if count == 0:
        max_value = i + 1
    elif count in s:
        max_value = max(max_value, i - s[count])
    else:
        s[count] = i

print(max_value)