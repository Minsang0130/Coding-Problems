from collections import Counter
def solution(s):
    d = Counter(s)
    result = []
    for i, j in d.items():
        if j == 1:
            result.append(i)
    result.sort()
    return ''.join(result)