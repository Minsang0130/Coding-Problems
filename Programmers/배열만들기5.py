def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if len(i)-l >0 and int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
    return answer
