def solution(myString, pat):
    answer = ""
    for ch in myString:
        if ch == "A":
            answer += "B"
        elif ch == "B":
            answer += "A"
        else:
            answer += ch
    # print(answer)
    for i in range(len(answer)):
        if answer[i:].startswith(pat):
            return 1

    return 0