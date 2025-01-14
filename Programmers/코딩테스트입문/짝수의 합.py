def solution(n):
    result = 0
    for num in range(n+1):
        if num % 2 == 0:
            result += num
    return result