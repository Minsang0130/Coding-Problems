def solution(spell, dic):
    count = 0
    is_true = len(spell)
    for i in dic:
        for j in spell:
            if j in i:
                count += 1
        if count == is_true:
            return 1
        else:
            count = 0
    return 2