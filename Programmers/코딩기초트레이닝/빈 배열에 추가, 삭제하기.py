def solution(arr, flag):
    X = []
    for idx, n in enumerate(arr):
        if flag[idx]:
            for _ in range(arr[idx] * 2):
                X.append(arr[idx])
        else:
            for _ in range(arr[idx]):
                X.pop()
    return X