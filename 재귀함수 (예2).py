def recursive_fun(n, m):
    if m == 0:
        return 1
    else:
        return recursive_fun(n, m-1) * n


n = int(input("N: "))

m = int(input("M: "))

print(recursive_fun(n, m))

#rf(4,5) = rf(4,4) * 4 = rf(4,0) * 4 * 4 * 4 * 4 * 4