import math
def solution(n):
    sqrt = math.isqrt(n)
    if sqrt * sqrt == n:
        return 1
    else:
        return 2