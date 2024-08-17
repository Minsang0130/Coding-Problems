def solution(numLog):
    num = 0
    answer = ''
    for i in range(0,len(numLog)-1):
        num = numLog[i+1] - numLog[i]
        if num == 1:
            answer += 'w'
        elif num == -1:
            answer += 's'
        elif num == 10:
            answer += 'd'
        elif num == -10:
            answer += 'a'
            
    return answer
