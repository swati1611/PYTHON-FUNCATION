def a(i):
    j=""
    index=len(i)
    while index>0:
        j=j+i[index-1]
        index=index-1
    return j
print(a('1234abcd'))