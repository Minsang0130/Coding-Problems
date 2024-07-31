import sys
from collections import deque
sys.stdin = open('sample_input.txt' , 'r')

T = int(input())

move_dict = {0: [1, 0], 1: [-1, 0], 2: [0, -1], 3: [0, 1]}

def solution(arr):
    # 점, 이동방향, 에너지 점수 q 저장 q
    dot_q = deque()
    time = 0
    for x, y, move, energy in arr:
        dot_q.append((x, y, move, energy))

    while time < 1000:
        time += 1

        for idx,




for test_case in (1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(arr)
    solution(arr)