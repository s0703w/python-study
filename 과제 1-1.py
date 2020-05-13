x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))

if x > y:
    if y >= z:
        print(y)
    else:
        if z > x:
            print(x)
        else:
            print(z)
else:
    if x > z:
        print(x)
    else:
        if z > y:
            print(y)
        else:
            print(z)

