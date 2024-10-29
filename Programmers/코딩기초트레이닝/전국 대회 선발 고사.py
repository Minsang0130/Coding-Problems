from collections import defaultdict

def solution(rank, attendance):
    sol_dict = defaultdict(int)
    result_list = []
    result = 0

    for idx, value in enumerate(rank):
        sol_dict[value] = idx

    for i in range(len(rank)):
        idx = sol_dict[i + 1]
        # 3명 추가 되면 종료
        if len(result_list) == 3:
            break

        # 참석 여부 호가인
        if attendance[idx]:
            result_list.append(idx)

    # 결과 값 계산
    for i in range(3):
        if i == 0:
            result += result_list[i] * 10000
        elif i == 1:
            result += result_list[i] * 100
        elif i == 2:
            result += result_list[i]

    return result