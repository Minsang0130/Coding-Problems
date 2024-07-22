import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def power_num(a, b):
    if b == 0:
        return 1
    else:
        return a * power_num(a, b - 1)


for test_case in range(1, T + 1):
    n = int(input())
    num, p_num = list(map(int, input().split()))
    print(f'#{test_case} {power_num(num, p_num)}')


# arr = [list(map(int, input().split())) for _ in range(N)]

# for 문 < 컴프리핸션
