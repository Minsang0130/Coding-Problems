def solution(myString, pat):
    pat_len = len(pat)
    count = 0
    for i in range(0, len(myString) - pat_len + 1):
        if myString[i:i + pat_len] == pat:
            count += 1
    return count