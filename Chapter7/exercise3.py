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
    
        numerator= factorial(4*k) * (1103 + 26390*k)
        
        denominator = factorial(k)**4 * 396**(4*k)
        
        term = factor * numerator / denominator
        
        
        total += term
        
        if (numerator/denominator) < 1e-15:
            break
        k += 1

    return 1 / total

if __name__ =="__main__":
    print(estimate_pi())
    print(math.pi)