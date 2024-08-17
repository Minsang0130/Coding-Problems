def solution(my_string, is_suffix):
    string_length = len(my_string)
    answer = []
    for i in range(0,string_length):
        answer.append(my_string[i:string_length+1])
    return 1 if is_suffix in answer else 0
