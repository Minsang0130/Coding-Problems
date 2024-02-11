def solution(arr, queries):
    for idx in range(0, len(queries)):
        i = queries[idx][0]
        j = queries[idx][1]
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    return arr
