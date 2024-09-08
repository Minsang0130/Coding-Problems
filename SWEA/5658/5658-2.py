import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = input()
    
    # 직사각형 한변당 들어가는 글자 수
    num = len(arr) // 4
    
    box = []
    temp_list = []
    for i in range(len(arr)):
        temp_list.append(arr[i])
        if (i + 1 ) // num == 0:
            box.append(temp_list)
            temp_list = []
    
    print(box)
    box = deque(box)
    print(box)