def solution(my_string, target):
    my_string = list(my_string)
    target = list(target)

    for chr in target:
        if chr not in my_string:
            return 0

    return 1