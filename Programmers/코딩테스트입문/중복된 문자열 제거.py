def solution(my_string):
    preChar = []
    result = ""
    for ch in my_string:
        if ch not in preChar:
            preChar.append(ch)
            result += ch
        else:
            continue
    return result