def solution(arr):
    start_idx = -1
    last_idx = -1
    for idx, i in enumerate(arr):
        if start_idx == -1 and i == 2:
            start_idx = idx
        if start_idx != -1 and i == 2:
            last_idx = idx
    if start_idx != -1 and last_idx == -1:
        return arr[start_idx:start_idx+1]
    elif start_idx != -1 and last_idx != -1:
        return arr[start_idx:last_idx+1]
    else:
        return [-1]