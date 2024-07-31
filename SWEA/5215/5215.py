import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(idx, cal_sum, score_sum):
    global answer

    if cal_sum > L:
        return

    if idx == N:
        answer = max(answer, score_sum)
        return

    dfs(idx + 1, cal_sum + arr[idx][1], score_sum + arr[idx][0])
    dfs(idx + 1, cal_sum, score_sum)


T = int(input())


for test_case in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    print(N, L, arr)

    dfs(0, 0, 0)
    print(f'#{test_case} {answer}')