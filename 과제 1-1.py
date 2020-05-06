x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))

if x > y > z:
    print(y)
if z > y > z:
    print(y)
elif y > z > x:
    print(z)