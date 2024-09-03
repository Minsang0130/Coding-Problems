import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

def find_parent(x):
    if x != p[x]:
        p[x] = find_parent(p[x])
    return p[x]

def union(x, y):
    px = find_parent(x)
    py = find_parent(y)``

    if px != py:
        if px < py:
            p[x] = py
        else:
            p[y] = px

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    p = list(range(N+1))

    for i in range(M):
        try:
            union(arr[i][0], arr[i][1])
        except:
            continue

    for i in range(len(p)):
        p[i] = find_parent(i)

    # print(p)
    print(f'#{test_case} {len(set(p))-1}')
    
# test_case 5개만 맞음 / edge 케이스 찾기