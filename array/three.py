# def y(*k):
#     i=max(list(k))
#     return[x-i for x in k]
# print(y(10,20,30,2,4,6,1))

# def e(n):
#     if n>=0:
#         print(n)
#         return e(n-1)
#         # return e(n+1)
    
# e(int(input("enter number")))


# def x(*k):
#     i=sum(list(k))
#     return[x+i for x in k]
# print(x(10,20,30,2,4,6,1))


# n=int(input("enter number:"))
def fact(n):
    if n<=1:
        return 1
    return(n*fact(n-1))
print(fact(5))
