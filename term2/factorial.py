def fac(n):
    if n == 0:
        return 1
    elif n < 2:
        return n
    else:
        return fac(n-1) * n

print(fac(10))
