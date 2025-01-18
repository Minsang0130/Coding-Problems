def solution(n):
    count = 0 # 순서쌍 개수
    for num1 in range(1,n+1):
        for num2 in range(1,n+1):
            mul_result = num1 * num2
            if mul_result == n:
                count += 1
            if mul_result > n:
                break
    return count