def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_set = set(dice)
    
    if len(dice_set) == 1:
        return 1111 * dice[0]
    
    if len(dice_set) == 2:
        p, q = dice_set
        if dice.count(p) == 2 and dice.count(q) == 2:
            return (p + q) * abs(p - q)
        elif dice.count(p) == 3:
            return (10 * p + q) ** 2
        else:
            return (10 * q + p) ** 2
    
    if len(dice_set) == 3:
        p, q, r = dice_set
        if dice.count(p) == 2:
            return q * r
        elif dice.count(q) == 2:
            return p * r
        elif dice.count(r) == 2:
            return p * q
        else:
            return min(dice_set) * 2
