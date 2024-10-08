def solution(arr):
    result = []
    for i in arr:
        result = result + [i] * i
    return result