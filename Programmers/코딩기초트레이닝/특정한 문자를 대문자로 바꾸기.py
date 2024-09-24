def solution(my_string, alp):
    result = []
    for ch in my_string:
        if ch == alp:
            result.append(ch.upper())
        else:
            result.append(ch)

    return ''.join(result)