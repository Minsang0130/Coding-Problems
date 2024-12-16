# def solution(array):
#     max_num = -1
#     max_count = -1
#     for num in set(array):
#         num_count = array.count(num)
#         if num_count > max_count:
#             max_num = num
#             max_count = num_count
#         elif num_count == max_count:
#             return -1
#         else:
#             return 1
#     return max_num
from collections import defaultdict
def solution(array):
    d = defaultdict(int)
    max_num = -1
    max_count = -1
    for num in array:
        d[num] += 1
    for key, value in d.items():
        if value > max_count:
            max_num = key
            max_count = value
    for key, value in d.items():
        if value == max_count and key != max_num:
            return -1
    return max_num

print(solution([1, 2, 3, 3, 3, 4]))