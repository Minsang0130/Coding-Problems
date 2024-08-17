def solution(num_list):
    last_num = len(num_list)-1
    if num_list[last_num] > num_list[last_num-1]:
        num_list.append(num_list[last_num] - num_list[last_num-1])
    else :
        num_list.append(num_list[last_num]*2)
    return num_list