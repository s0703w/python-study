def recursive_function(n):
    if n==0:
        return n
    else:
        return recursive_function(n-1) + n

print(recursive_function(10))