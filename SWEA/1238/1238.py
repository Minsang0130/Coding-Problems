import sys
sys.stdin = open('input.txt', 'r')
from collections import defaultdict, deque

def bfs(start_v):
    q = deque([(start_v, 0)])
    while q:
        v, cnt = q.popleft()
        for adj_v in num_dic[v]:
            if visited[adj_v] == 0:
                visited[adj_v] = cnt + 1
                q.append((adj_v, cnt+1))

for test_case in range(1, 11):
    N, start_num = map(int, input().split())
    arr = list(map(int, input().split()))
    num_dic = defaultdict(list)

    visited = [0] * (101)
    for i in range(N // 2):
        num_dic[arr[i*2]].append(arr[i*2 + 1])

    bfs(start_num)

    max_num = max(visited)

    for i in range(len(visited) -1, -1, -1):
        if max_num == visited[i]:
            result = i
            break

    # print(num_dic)
    print(f'#{test_case} {result}')