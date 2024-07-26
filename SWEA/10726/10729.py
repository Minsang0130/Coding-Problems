# import sys
# sys.stdin = open("input.txt", "r")

def is_on_off(bit_num, num):
    b_num = list(str(bin(num)))
    # return b_num
    # return b_num[:bit_num:-1]
    if set(b_num[-bit_num:]) == {'1'}:
        return 'ON'
    else:
        return 'OFF'


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    print(f'#{test_case} {is_on_off(n, m)}')
