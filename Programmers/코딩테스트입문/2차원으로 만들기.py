def solution(num_list, n):
    temp_list = []
    result_list = []
    for num in num_list:
        temp_list.append(num)
        
        if len(temp_list) == n:
            result_list.append(temp_list)
            temp_list = []
    return result_list