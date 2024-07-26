import sys
sys.stdin = open('sample_input.txt', 'r')

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
result = []

def dfs(dx, dy, deepth, result) :
    if deepth == 7:
        return

    for nx, ny in dxy:
        dx = dx + nx
        dy = dy + ny
        if dx < 0 or dx >= 4 or dy < 0 or dy >= 4:
            continue
        result.append(arr[dx][dy])
        dfs(dx, dy, deepth+1, result)


T = int(input())
arr = []
for test_case in range(4):
    arr.append(list(input().split()))

print(arr)
for i in range(4):
    for j in range(4):
        print(dfs(i, j, 0, result))

