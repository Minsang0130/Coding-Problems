def solution(s):
    result = 0
    s = s.split()
    for idx, i in enumerate(s):
        if i == "Z":
            result -= int(s[idx-1])
        else:
            result += int(i)
    return result