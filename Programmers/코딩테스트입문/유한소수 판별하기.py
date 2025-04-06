def solution(a, b):
    import math
    g = math.gcd(a, b)
    b //= g

    for p in [2, 5]:
        while b % p == 0:
            b //= p

    return 1 if b == 1 else 2