def solution(numbers, k):
    throwIdx = 1
    for i in range(1,k):
        throwIdx += 2
        if throwIdx > len(numbers):
            throwIdx %= len(numbers)
    
    return throwIdx