def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        result = 1
        for i in range(len(num_list)):
            result *= num_list[i]
        return result
                                