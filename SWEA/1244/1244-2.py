import sys
sys.stdin = open('input.txt', 'r')
# import itertools

T = int(input())

def solution(num_list, n, max_num):
    global result

    max_num = int(''.join(num_list))

    if n == 0:
        if max_num > result:
            result = max_num
        return
    
    key = (tuple(num_list), n)
    if key in visited:
        return
    visited.add(key)

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num_list[i], num_list[j] = num_list[j], num_list[i]

            solution(num_list, n - 1, max_num)

            num_list[i], num_list[j] = num_list[j], num_list[i]


for test_case in range(1, T+1):
    num, n = input().split()
    n = int(n)
    num_list = list(num)
    visited = set()
    result = 0

    solution(num_list, n, 0)

    print(f'#{test_case} {result}')
    
#     # 값이 다른 숫자 개수 세는 변수
#     count = 0
#     result = 0

#     # 모든 경우의 조합을 저장하는 리스트
#     shuffle_num_list = []

#     # 조합 생성
#     for i in itertools.permutations(num_list, len(num_list)):
#         # shuffle_num_list.append(int(''.join(i)))
#         shuffle_num_list.append(i)
    
#     # 값이 원래 값하고 차이나는 개수 (N * 2) 인 숫자 확인
#     for i in range(len(shuffle_num_list)):
#         for j in range(len(shuffle_num_list[i])):
#             if num_list[j] != shuffle_num_list[i][j]:
#                 count += 1
#         if count <= n*2:
#             result = max(result, int(''.join(shuffle_num_list[i])))
#         count = 0
            

#     print(result)