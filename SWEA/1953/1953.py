import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input())) for _ in range(T)]
