def solution(my_string, m, c):
    sentence = ''
    idx = c-1
    while idx < len(my_string):
        sentence += my_string[idx]
        idx += m
    return sentence
