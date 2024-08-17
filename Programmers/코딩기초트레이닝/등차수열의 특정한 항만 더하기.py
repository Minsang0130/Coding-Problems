def solution(a, d, included):
    num = a
    sum = 0
    num_list = [a,]
    for i in range(0,len(included)):
        num += d
        num_list.append(num)
        if num_list[i]*included[i]!= 0:
            sum += num_list[i]
    return sum

print(solution(3,4,[True, False, False, True, True]))