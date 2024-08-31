def solution(num_list):
    hol = sum([num_list[i] for i in range(len(num_list)) if i % 2 != 0])
    jjack = sum([num_list[i] for i in range(len(num_list)) if i % 2 == 0])
    return max(hol,jjack)