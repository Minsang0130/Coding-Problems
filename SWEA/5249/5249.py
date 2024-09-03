import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        p[px] = py
    else:
        p[py] = px

def mst_kruskal(edges):
    result = 0
    
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        s, e, w = edge

        if find_set(s) != find_set(e):
            union(s, e)
            result += w

    return result

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    p = list(range(V+1))
    # print(arr)
    print(f'#{test_case} {mst_kruskal(arr)}')
    