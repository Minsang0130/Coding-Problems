def solution(num_list):
    multiply = 1
    num_sum = 0
    for i in num_list :
        multiply *= i
        num_sum += i
    return 1 if multiply < num_sum*num_sum else 0