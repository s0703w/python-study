y = str(input("Y: "))
m = str(input("M: "))
d = str(input("D: "))


def function(y, m, d):
    year = ''
    if int(y) >= 1000:
        year = y
    elif int(y) >= 100:
        year = "0" + y
    elif int(y) >= 10:
        year = "00" + y
    else:
        year = "000" + y
    month = ''
    if int(m) >= 10:
        month = m
    else:
        month = "0" + m
    day = ''
    if int(d) >= 10:
        day = d
    else:
        day = "0" + m
    return year + ":" + month + ":" + day


print(function(y, m, d))
