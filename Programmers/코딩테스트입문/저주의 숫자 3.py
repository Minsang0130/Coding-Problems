def solution(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if num % 3 != 0 and '3' not in str(num):
            count += 1
    return num
