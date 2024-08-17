def solution(arr, idx):
    for idx in range(idx, len(arr)):
        if arr[idx] == 1:
            return idx
    return -1