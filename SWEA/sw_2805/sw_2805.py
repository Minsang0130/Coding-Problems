import sys
sys.stdin = open("input.txt", "r")


def arr_calculate(a):  # 점수 계산 함수
    result = 0
    start_num = int(len(a) / 2)  # 시작 인덱스
    end_num = int(len(a) / 2)  # 끝 인덱스
    count = 0  # 몇번째 계산인지
    count_max = int(len(a) / 2)  # 증가 계산 최대 개수

    for i in range(0, len(a)):  # 리스트의 열 개수 만큼 반복
        for j in range(start_num, end_num+1):  # 해당 열의 농장 구역의 값들을 더한 후 result에 저장
            result += a[i][j]
        if count < count_max and start_num != 0:  # 영역이 커지는 조건: 현재 계산이 증가 계산 최대보다 작고 시작숫자가 0이 아닐때
            start_num -= 1
            end_num += 1
            count += 1
        else:  # 영역이 작아지는 조건
            end_num -= 1
            start_num += 1
    return result


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    print(f'#{test_case} {arr_calculate(arr)}')
