def solution(i, j, k):
    target = str(k)
    count = 0
    for n in range(i, j + 1):
        count += str(n).count(target)
    return count