def solution(my_string, indices):
    # my_string의 인덱스 set
    str_idx= set(range(0, len(my_string)))
    
    # 지워야할 인덱스 set
    remove_idx = set(indices)

    # 차집합을 통한 결과 set 저장
    result_idx = str_idx - remove_idx

    # 결과 저장 변수
    result = ''

    # set를 list로 변경후 정렬, set는 순서가 없으므로 인덱스 순서가 섞여 있음
    result_idx = list(result_idx)
    result_idx.sort()

    # 인덱스 순서대로 불러와 result에 저장
    for idx in result_idx:
        result += my_string[idx]
    return result