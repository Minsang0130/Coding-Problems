def solution(numbers):
    result = -99999999999999999
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            num = numbers[i] * numbers[j]
            if num > result:
                result = num
    return result