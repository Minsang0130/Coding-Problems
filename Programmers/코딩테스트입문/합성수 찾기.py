def solution(n):
    count = 0
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
    return count