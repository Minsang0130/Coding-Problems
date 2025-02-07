def solution(my_string):
    moum = ['a', 'e', 'i', 'o', 'u']
    for ch in moum:
        my_string = my_string.replace(ch,'')
    return my_string