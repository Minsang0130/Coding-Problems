import sys
sys.stdin = open("sample_input.txt", "r")

# 벽돌 레이저
def brick_lazer(arr):
    arr_list = []   # 스택
    result = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            arr_list.append(arr[i])
            # print(arr_list)
        if arr[i] == ')':
            arr_list.pop()
            if arr[i-1] == '(':
                result += len(arr_list)
            if arr[i-1] == ')':
                result += 1
    return result


T = int(input())
for test_case in range(1, T + 1):
    arr = list(input())
    print(f'#{test_case} {brick_lazer(arr)}')
