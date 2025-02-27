def solution(numbers):
    alpha_dict = { "one" : '1', "two" : '2', "three" : '3', "four" : '4', "five": '5', "six":'6', "seven" : '7', "eight" : '8', "nine":'9', "zero" : '0'}
    result = ""
    temp = ""
    for i in numbers:
        temp += i
        if temp in alpha_dict.keys():
            result += alpha_dict[temp]
            temp = ""
    return int(result)