def a(x,y,z):
    if x>y and x>z:
        print("x is maximum")
    elif y>x and y>z:
        print("y is maximum")
    elif z>x and z>y:
        print("z is maximum")
    else:
        print("not")
a(4,7,6)