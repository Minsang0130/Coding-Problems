import sys
sys.stdin = open('input.txt', 'r')


def decrypt_array(encrypted_list):
    idx = 0
    temp = 0
    while encrypted_list[idx] != 0:
        temp = encrypted_list[0] + 1
        arr.

        if idx == len(arr):
            idx = 0

for test_case in range(1, 11):
    case_num = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case} {arr}')
