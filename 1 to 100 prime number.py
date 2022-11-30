def fun(a):
    i=1
    while i<a:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c=c+1
            j=j+1
        if c==2:
            print(i,"prime number")
        else:
            print(i,"not prime")
        i=i+1
fun(100)