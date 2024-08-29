import sys
sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())

def solution(N):
    arr = [0] * (N+1)
    
    for n in range(1, N+1):
        if n == 1:   
            arr[n] = 1
        elif n == 2:   
            arr[n] = 3
        elif n == 3:   
            arr[n] = 6
        else:
            arr[n] = arr[n-1] + arr[n-2] * 2 + arr[n-3]
    
    return arr[N]

for test_case in range(1, T+1):
    N = int(input())
    
    print(f'#{test_case} {solution(N)}')