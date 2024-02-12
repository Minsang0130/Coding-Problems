def solution(arr, queries):
    for a,b,c in queries : 
        for idx in range(a,b+1):
            if idx % c == 0:
                arr[idx] += 1
    return arr
