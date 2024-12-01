def solution(picture, k):
    result = []  # 확대된 그림을 저장할 리스트
    for row in picture:  # 그림의 각 행(row)을 반복
        expanded_row = ""  # 한 행을 k배로 늘린 결과를 저장
        for char in row:  # 행의 각 문자를 k번 반복
            expanded_row += char * k
        for _ in range(k):  # k번 반복하여 행도 k배 늘림
            result.append(expanded_row)
    return result