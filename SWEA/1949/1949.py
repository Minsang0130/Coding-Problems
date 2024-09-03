

import sys
import pprint
sys.stdin = open('sample_input.txt', 'r')

dxy = [[1,0], [-1,0], [0,1], [0,-1]]

def solution(x, y, depth, visited, chance):
    global result
    
    # pprint.pprint(arr)
    # pprint.pprint(visited)
    # print(depth)
    
    if arr[x][y] <= 1 :
        if result < depth:
            result = max(depth, result)
            # pprint.pprint(arr)
            # pprint.pprint(visited)
            # print(depth)
        # print(result)
        return
    
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if arr[nx][ny] >= arr[x][y] and chance and arr[nx][ny] - K < arr[x][y]:
                if arr[nx][ny] - K < 0:
                    arr[nx][ny] -= K
                    visited[nx][ny] = True
                    solution(nx, ny, depth + 1, visited, False)
                    visited[nx][ny] = False
                    arr[nx][ny] += K
                    
                    
                else:
                    arr[nx][ny] -= 1
                    visited[nx][ny] = True
                    solution(nx, ny, depth + 1, visited, False)
                    visited[nx][ny] = False
                    arr[nx][ny] += 1
                
            elif arr[nx][ny] < arr[x][y]:
                visited[nx][ny] = True
                solution(nx, ny, depth + 1, visited, True)
                visited[nx][ny] = False
    
    # visited[x][y] = False

    
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
        
    result = 0
    max_num = 0
    max_num_list = []
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if max_num < arr[i][j]:
                max_num = arr[i][j]
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if max_num == arr[i][j]:
                max_num_list.append([i,j])
    
    
    for i in range(len(max_num_list)):
        x, y = max_num_list[i][0], max_num_list[i][1]
        visited = [[False] * N for _ in range(N)]
        visited[x][y] = True
        solution(x, y, 1, visited, True)
        
    print(f'#{test_case} {result}')