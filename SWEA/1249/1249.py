import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

T = int(input())

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

'''
def bfs(n, x, y):
    q = deque([(0, 0, 0)])
    result = []

    while q:
        x, y, time = q.popleft()

        if x == n - 1 and y == n - 1:
            result.append(time)

        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny, time + road[nx][ny]))

                visited[nx][ny] = True
    return min(result)
'''


def bfs(x, y):
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            if 0 <= nx < num and 0 <= ny < num:
                if visited[nx][ny] > visited[x][y] + road[nx][ny]:
                    visited[nx][ny] = visited[x][y] + road[nx][ny]
                    q.append((nx, ny))

    return visited[num-1][num-1]


for test_case in range(1, T+1):
    num = int(input())
    road = [list(map(int, input())) for _ in range(num)]

    visited = [[float('inf')] * num for _ in range(num)]
    visited[0][0] = 0

    print(f'#{test_case} {bfs(0, 0)}')
