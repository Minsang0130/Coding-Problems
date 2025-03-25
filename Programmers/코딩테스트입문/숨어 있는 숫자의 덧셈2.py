import re

def solution(my_string):
#     num_list = ['0','1','2','3','4','5','6','7','8','9']
#     result = ""
#     for i in range(0, len(my_string) - 1):
#         if my_string[i] in num_list and my_string[i+1] in num_list:
#             result += my_string[i]
#         elif my_string[i] in num_list and my_string[i+1] not in num_list:
#             result += my_string[i] + '+'
    
#     return eval(result[:-1])

    numbers = re.findall(r'\d+', my_string)  # 숫자로 이루어진 문자열 추출
    return sum(map(int, numbers))