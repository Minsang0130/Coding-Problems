import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(idx, num_sum):
    global result

    if num_sum == K:
        print(idx, num_sum)
        result += 1
        return

    # if num_sum >= K:
    #     return

    if idx == N:
        return

    # 선택한 경우
    dfs(idx + 1, num_sum + arr[idx])
    dfs(idx + 1, num_sum)


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    #1 재귀하다 종료 해줄 거
    #2 누적 점수 합계
    dfs(0, 0)

    print(f'#{test_case} {result}')