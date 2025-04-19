def solution(A, B):
    n = len(A)
    for k in range(n):
        # 오른쪽으로 k만큼 밀기: A[-k:] + A[:-k]
        if A[-k:] + A[:-k] == B:
            return k
    return -1