def number(limit):
    for i in range(1,limit+1):
        if i%2==0:
            print(i,"not prime")
        else:
            print(i,"prime")
number(12)