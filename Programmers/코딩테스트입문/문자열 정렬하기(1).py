def solution(my_string):
    numlist = ['1','2','3','4','5','6','7','8','9','0']
    result = []
    for ch in my_string:
        if ch in numlist:
            result.append(int(ch))
    result.sort()
    return result