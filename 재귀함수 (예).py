def recursive_function(n):
    if n == 1:
        return n
    else:
        return recursive_function(n - 1) * n


n = int(input("N: "))
print(recursive_function(n))
