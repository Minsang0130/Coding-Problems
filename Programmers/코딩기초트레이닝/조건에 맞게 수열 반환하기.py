def solution(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0 and arr[i] < 50:
            result.append(arr[i] * 2)
        elif arr[i] % 2 == 0 and arr[i] >= 50:
            result.append(arr[i] // 2)
        else:
            result.append(arr[i])
    return result