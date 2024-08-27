import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            union(x, y)
            rank[px] += 1

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [0] * (N + 1)
    rank = [0] * (N + 1)

    for i in range(1, N+1):
        make_set(i)
    
    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])
        print(p)
        # print(rank)
        print('----')

    p = set(p)
    # print(p)
    print(f'#{test_case} {len(p) - 1}')
