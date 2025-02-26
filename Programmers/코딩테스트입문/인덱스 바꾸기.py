def solution(my_string, num1, num2):
    ch1 = my_string[num1]
    ch2 = my_string[num2]
    result = ""
    for idx, i in enumerate(my_string):
        if idx == num1:
            result += ch2
        elif idx == num2:
            result += ch1
        else:
            result += i
    return result