def fun(n):
    for i in range(2, n):
        if n % i != 0:
            return False
    return True


n = int(input("N: "))
print(fun(n))