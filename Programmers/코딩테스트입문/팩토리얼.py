def solution(n):
    arr = [1] * 10
    for i in range(1, 10):
        arr[i] = arr[i-1] * (i+1)
    arr.reverse()
    for idx, j in enumerate(arr):
        if n >= j:
            return 10 - idx