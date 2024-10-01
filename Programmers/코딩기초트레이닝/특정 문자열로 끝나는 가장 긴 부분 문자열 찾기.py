def solution(myString, pat):
    result_idx = 0
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            result_idx = i

    return myString[:result_idx + len(pat)]

print(solution("AbCdEFG", "dE"))