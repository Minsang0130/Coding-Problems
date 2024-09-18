def solution(num_list):
    count = 0
    for i in range(len(num_list)):
        temp = num_list[i]
        while temp != 1:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = (temp - 1) // 2
            count += 1
    return count