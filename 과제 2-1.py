def function(x, y, z):
    if x > y:
        if y >= z:
            return y
        else:
            if z > x:
                return x
            else:
                return z
    else:
        if x > z:
            return x
        else:
            if z > y:
                return y
            else:
                return z


x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))

print(function(x, y, z))

a = [x, y, z]
a.sort()
print(a[1])