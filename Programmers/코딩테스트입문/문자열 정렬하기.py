def solution(string):
    my_string = ""
    for ch in string:
        my_string += ch.lower()
    my_string = list(my_string)
    my_string.sort(key = lambda x: ord(x))
    return "".join(my_string)