def solution(my_string, queries):
    temp = ''
    my_string = list(my_string)
    for i,j in queries:
        h = j
        for i in range(i,int((i+j)/2)+1):
            temp = my_string[h]
            my_string[h] = my_string[i]
            my_string[i] = temp
            h -= 1
            
    return "".join(my_string)
