def solution(bin1, bin2):
    # 두 이진수를 정수로 변환 (기수 2)
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    # 두 정수의 합을 구합니다.
    total = num1 + num2
    # 합을 이진수로 변환한 후, 접두어 '0b'를 제거하여 문자열로 반환합니다.
    return bin(total)[2:]