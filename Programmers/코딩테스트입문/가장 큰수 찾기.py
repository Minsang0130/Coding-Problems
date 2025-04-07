def solution(array):
    sorted_array = sorted(array)
    return [sorted_array[-1], array.index(sorted_array[-1])]