p = int(input("N1: "))
y = int(input("N2: "))
t = int(input("N3: "))
h = int(input("N4: "))
o = int(input("N5: "))
n = int(input("N6: "))
w = int(input("N7: "))
u = int(input("N8: "))
r = int(input("N9: "))
k = int(input("N10: "))

a = [p, y, t, h, o, n, w, u, r, k]
l = len(a)


def function(a):
    for i in range(l):
        return (a[i - 1] + a[i]) % 10



print(function(a))
