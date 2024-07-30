import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')


def solution(arr, N, K):
    q = deque(arr)
    count = 0

    # 한 변당 위치하는 숫자 개수 (사각형이므로 4개로 나눔)
    slice_num = N // 4

    # 최솟값 초기화
    min_num = '4934u90130u314i'

    # 결과 값 배열
    result_arr = []

    # 회전하다 0회전과 같아지면 멈춤
    while count < slice_num:
        # 회전 한뒤 q의 값을 갱신
        arr = list(q)
        
        # 한변당 만들어진 수를 배열에 저장
        sliced_list = ["".join(arr[i:i + slice_num]) for i in range(0, len(q), slice_num)]
        
        # 결과 저장 배열에 만들어진 숫자들 추가
        result_arr.append(sliced_list)
        
        # 회전
        q.append(q.popleft())
        
        # 회전 횟수 증가
        count += 1

    # 2차원 배열을 1차원 배열로 변경
    result_arr = [item for row in result_arr for item in row]
    
    # 중복값 제거
    result_arr = list(set(result_arr))
    
    # 내림차순으로 정렬
    result_arr = sorted(result_arr, reverse=True)
    # print(result_arr)
    # print(int(result_arr[K-1], 16))
    
    # K번째로 큰 값을 10진수로 반환
    return int(result_arr[K-1], 16)


# 테스트 케이스 개수
T = int(input())

# 숫자의 개수 % 4 == 0, 크기 순서 K(K번째로 큰 값)

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())

    print(f'#{test_case} {solution(arr, N, K)}')

