a = [5, 3, 2, 6, 4, 7, 1, 8]
l = len(a)

for i in range(l):
    for j in range(i + 1, l):
        print(i, j, a)
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)