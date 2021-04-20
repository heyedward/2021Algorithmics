def exp(base, power):
    if power == 0:
        return 1
    if power > 0 and power % 2 == 0:
        return exp(base, power//2) ** 2
    elif power % 2 != 0:
        return exp(base, power//2) ** 2 * base

print(exp(3,12))
