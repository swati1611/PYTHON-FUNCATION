# def factorial(n):
#     if (n<=1):
#         return 1
#     else:
#         return(n*factorial(n-1))
# n=int(input("enter"))
# print("factorial:")
# print(factorial(n))


# n=n*(n-1)*(n-2)*(n-3)*1
# n=5*(5-1)*(5-2)*(5-3)*1
# print(n)


# def n(a):
#     if a==70:
#         print(70)
#     else:
#         print(a)
#         n(a+7)
# n(7)

# def n(a):
#     if a==70:
#         print(70)
#     else:
#         if a%7==0:
#             print(a)
#         n(a+1)
# n(1)

# def n(a):
#     if a==3:
#         print(a*'*')
#     else:
#         print(a*'*')
#         n(a+1)
# n(1)

# def n(a):
#     if a==75:
#         pass
#     else:
#         print(a-64)
#         n(a+1)
# n(65)


def n(a):
    if a==75-65:
        print(a)
    else:
        if a%1==0:
            print(a)
        n(a+1)
n(1)