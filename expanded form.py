# a="12345"
# i=0
# while i<len(a):
#     j=len(a)-(i+1)
#     b=int(a[i])*10**j
#     i=i+1
#     print("+",b,end=" ")


a=input("enter")
i=0
while i<len(a):
    j=len(a)-(i+1)
    b=int(a[i])*10**j
    i=i+1
    print("+",b,end=" ")
