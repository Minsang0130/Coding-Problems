def solution(my_string):
    string_length = len(my_string)
    answer = []
    for i in range(0,string_length):
        answer.append(my_string[i:string_length+1])
        
    answer = sorted(answer)
    return answer
