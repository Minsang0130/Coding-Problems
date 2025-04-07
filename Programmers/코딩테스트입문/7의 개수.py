def solution(array):
    count = 0
    for num in array:
        for n in str(num):
            if n == '7':
                count += 1
    return count