def solution(num_str):
    result = 0
    for idx in range(len(num_str)):
        result += int(num_str[idx])
    return result