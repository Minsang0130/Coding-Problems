import sys
sys.stdin = open('sample_input.txt', 'r')

def solution(num, sentence):
    global result

    if len(sentence) == num_string:
        result.add(sentence)
        return
    # print(result)
    
    for key in num_dict.keys():
        if num_dict[key] != 0:
            if sentence[-1] + '1' == key:
                num_dict[key] -= 1
                solution(num + 1, sentence + '1')
                num_dict[key] += 1
            elif sentence[-1] + '0' == key:
                num_dict[key] -= 1               
                solution(num + 1, sentence + '0')
                num_dict[key] += 1
    
    # print(result)
    if num >= len(arr):
        return
    # solution(num + 1, sentence)
    
# 사용 가능한 문자 리스트 만드는 함수
# def add_item(arr, num, idx):
#     if idx == 0:
#         for i in range(num):
#             arr.append('00')
    
#     elif idx == 1:
#         for i in range(num):
#             arr.append('01')
    
#     elif idx == 2:
#         for i in range(num):
#             arr.append('10')

#     elif idx == 3:
#         for i in range(num):
#             arr.append('11')

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    num_string = sum(arr) + 1
    # 사용 가능한 숫자들
    # num_list = []

    # for idx in range(0, len(arr)):
    #     if arr[idx] != 0:
    #         add_item(num_list, arr[idx], idx)
    
    # 가능한 문자 dict
    num_dict = {'00': arr[0], '01': arr[1], '10': arr[2], '11' : arr[3]}

    # 인덱스 번호
    # idx_num = 0

    # 입력값에 맞게 dict 구성
    # for key in num_dict.keys():
    #     if arr[idx_num] != 0:
    #         num_dict[key] = arr[idx_num]
    #     idx_num += 1
    
    # print(num_dict)
    result = set()

    # 문자열 시작 값 4가지 경우('00', '01', '10', '11'로 시작)
    for key in num_dict.keys():
        if num_dict[key] != 0:
            num_dict[key] -= 1
            solution(0, key)
            num_dict[key] += 1

    # 입력값에 값이 1개만 있는 경우가 아니면 결과 값에서 key값만 있는 값 삭제
    if num_string == 1:
        for key in num_dict.keys():
                result.add(key)
    
    # # result set에 값이 있으면 맨 첫번째 값
    # if result:
    #     # result = [s for s in result if len(s) == num_string + 1]
    #     result = list(result)
    #     print(f'#{test_case} {result[0]}')
    # # 없으면 impossible
    # else:
    #     result = 'impossible'
    #     print(f'#{test_case} {result}')

    
    
