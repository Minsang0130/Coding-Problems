def solution(strArr):
    result = []
    for word in strArr:
        if "ad" in word:
            continue
        else:
            result.append(word)
    return result