def solution(my_string, s, e):
    my_string = list(my_string)
    answer = list(my_string[s:e+1])
    answer = answer[::-1]
    print(answer)
    k = 0
    for i in range(s,e+1):
        my_string[i] = answer[k]
        k+=1
    return ''.join(my_string)
