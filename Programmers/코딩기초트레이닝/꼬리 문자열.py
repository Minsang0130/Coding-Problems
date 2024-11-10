def solution(str_list, ex):
    result = ""
    for ch in str_list:
        if ex not in ch:
            result += ch
    return result