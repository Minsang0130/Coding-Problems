def solution(my_string):
    my_string = list(my_string)
    numlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = 0
    for ch in my_string:
        if ch in numlist:
            result += int(ch)
    return result