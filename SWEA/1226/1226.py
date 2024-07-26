import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(x, y):
    q = deque([(1, 1)])

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and arr[nx][ny] != 1:
                q.append((nx, ny))

                visited[nx][ny] = True

                if nx == 13 and ny == 13:
                    return 1
    return 0


for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True
    print(f'#{test_case} {bfs(1, 1)}')
