def solution(my_strings, parts):
    answer = ''
    idx = 0
    for i, j in parts:
        answer += str(my_strings[idx][i:j+1])
        idx += 1
        
    return answer
