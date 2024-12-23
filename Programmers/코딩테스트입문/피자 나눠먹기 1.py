def solution(n):
    pizza = 7
    count = 0
    while n > 0:
        n -= pizza
        count += 1
    return count