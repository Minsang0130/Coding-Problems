def solution(strArr):
    result = []
    for idx, ch in enumerate(strArr):
        if idx % 2 == 0:
            result.append(ch.lower())
        else:
            result.append(ch.upper())
    return result