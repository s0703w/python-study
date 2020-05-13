y = int(input("Y: "))
m = int(input("M: "))
d = int(input("D: "))
h = int(input("H: "))
mm = int(input("MM: "))


def function(y, m, d, h, mm):
    if y < 1000:
        return "0" + y
    if y < 100:
        return "00" + y
    if y < 10:
        return "000" + y
    else:
        return y


print(function(y, m, d, h, mm))
