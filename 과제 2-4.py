a = "-"
b = "+"
x = int(input("X: "))
o = str(input("O: "))
y = int(input("Y: "))


def function(x, o, y):
    if o == a:
        return x - y
    if o == b:
        return x + y


print(function(x, o, y))
