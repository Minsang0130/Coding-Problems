def solution(n):
    result = set()
    for i in range(2, n+1):
        while n % i == 0:
            result.add(i)
            n = n // i
        if n == 1:
            break
    result = list(result)
    result.sort()
    return result