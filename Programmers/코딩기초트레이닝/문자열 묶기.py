from collections import defaultdict

def solution(strArr):
    d = defaultdict(int)
    for ch in strArr:
        d[len(ch)] += 1
    return max(d.values())