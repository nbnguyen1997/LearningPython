import math


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
    # for k in range(1,10):
        numerator= factorial(4*k) * (1103 + 26390*k)
        
        denominator = factorial(k)**4 * 396**(4*k)
        
        term = factor * numerator / denominator
        
        # print(k,numerator/denominator)
        total += term
        
        if (numerator/denominator) < 1e-15:
            break
        k += 1

    return 1 / total

print(estimate_pi())
# print(float(1e-2))
print(math.pi)