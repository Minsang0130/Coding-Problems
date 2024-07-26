import sys
sys.stdin = open("input.txt", "r")


def ispalindrome(s):
    start_num = 0
    end_num = len(s) - 1
    # 짝수 문자열일때 탈출 조건 변경
    if start_num >= end_num:
        return 1
    elif s[start_num] == s[end_num]:
        return ispalindrome(s[start_num+1:end_num])
    else:
        return 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sentence = str(input())
    print(f'#{test_case} {ispalindrome(sentence)}')
