def solution(num_list):
    odd_num = ''
    even_num = ''
    for i in num_list:
        if i % 2 ==0:
            even_num += str(i)
        else:
            odd_num += str(i)
    return eval(f"{even_num} + {odd_num}")

print(solution([3,4,5,2,1]))