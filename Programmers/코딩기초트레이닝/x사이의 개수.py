def solution(myString):
    count = 0
    result = []
    for ch in myString:
        if ch == 'x':
            result.append(count)
            count = 0
        else:
            count += 1
    result.append(count)
    return result