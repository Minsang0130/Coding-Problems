import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def solution(arr, rotation_num):
    idx = 0
    temp_idx = 0
    while rotation_num > 0:
        temp_idx = arr[:].index(min(arr))
        # print(temp_idx)
        if max(arr) == arr[idx]:
            arr[idx], arr[temp_idx] = arr[temp_idx], arr[idx]
            rotation_num -= 1
            idx = rotation_num
            print('temp!')
        else:
            idx += 1
    return arr


T = int(input())

for test_case in range(1, T+1):
    input_arr = list(input().split())
    num_arr = list(map(int, input_arr[0]))
    rotation_num = int(input_arr[1])
    print(solution(num_arr, rotation_num))
