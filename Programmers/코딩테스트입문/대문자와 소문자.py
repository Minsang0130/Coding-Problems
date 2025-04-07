def solution(my_string):
    result = ''
    for ch in my_string:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
    return result