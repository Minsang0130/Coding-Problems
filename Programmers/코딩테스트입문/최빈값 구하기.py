from collections import defaultdict
def solution(array):
    d = defaultdict(int)
    for num in array:
        d[num] += 1

    for num in d.values():

    return d

solution([1, 2, 3, 3, 3, 4])