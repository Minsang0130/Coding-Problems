import sys
sys.stdin = open('sample_input.txt', 'r')

# def solution(idx, left_arr, right_arr):

#     if idx == len(arr):
#         return

#     solution(idx + 1, )

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    M, A = map(int, input().split())


    left_arr = []
    right_arr = []

    solution(0, left_arr, right_arr)