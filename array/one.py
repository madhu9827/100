accounts = [
 [1, 2, 3],
 [3, 2, 1]
]
max=0
for acc in accounts:
    i=sum(acc)
    if i>max:
        max=i
print(max)
