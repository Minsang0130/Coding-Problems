def solution(n):
    result = 0
    n_list = list(str(n))
    for i in n_list:
        result += int(i)
    return result