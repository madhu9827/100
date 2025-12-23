nums = [8, 1, 2, 2, 3]

result = []

for i in nums:
    count = 0
    for j in nums:
        if j < i:
            count += 1
    result.append(count)

print(result)
