def solution(array, n):
    p_difference = 101
    result = 101
    for i in array:
        difference = abs(i - n)
        if difference == p_difference and result > i:
            result = i
        elif p_difference > difference:
            p_difference = difference
            result = i
            
    return result