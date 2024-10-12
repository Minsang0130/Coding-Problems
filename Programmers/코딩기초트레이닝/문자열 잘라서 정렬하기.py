def solution(myString):
    result = myString.split("x")
    result.sort()
    real_result = []
    for idx, ch in enumerate(result):
        if ch != "":
            real_result.append(ch)
    return real_result