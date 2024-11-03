def solution(n_str):
    result = ""
    for idx in range(len(n_str)):
        if n_str[idx] != '0':
            result = n_str[idx:]
            break
    return result