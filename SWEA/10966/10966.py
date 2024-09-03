import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

T = int(input())

def solution(visited):
    q = deque()
    n = len(arr)
    result = 0

    for i in range(n):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 0

    dxy = [[1,0], [-1,0], [0,1], [0,-1]]

    while q:
        cx, cy = q.popleft()
        
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 > nx or nx >= N or 0 > ny or ny >= M: continue

            if visited[nx][ny] != -1: continue

            q.append((nx, ny))
            visited[nx][ny] = visited[cx][cy] + 1
    
    for i in range(n):
        for j in range((len(arr[i]))):
            result += visited[i][j]
    
    return result
                

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    
    print(f'#{test_case} {solution(visited)}')