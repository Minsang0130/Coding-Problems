def solution(num_list):
    jjack = 0
    hol = 0
    for num in num_list:
        if num % 2 == 0 :
            jjack += 1
        else:
            hol += 1
    return [jjack, hol]