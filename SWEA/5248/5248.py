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
            # 자식들에게 부모의 값을 주기 위해 했지만 자식들 전부에게 갱신이 안됨
            # union(x, y)
            rank[px] += 1

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [0] * (N + 1)
    rank = [0] * (N + 1)

    for i in range(1, N+1):
        make_set(i)
    
    for i in range(M):
        union(arr[i * 2], arr[i*2 +1])
        # print(p)
        # print(rank)
        # print('----')

    # p의 모든 값에 부모들을 갱신
    for i in range(1, N + 1):
        p[i] = find_set(p[i])
    p = set(p)
    # print(p)
    print(f'#{test_case} {len(p) - 1}')
