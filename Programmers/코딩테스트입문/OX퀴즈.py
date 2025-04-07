def solution(quiz):
    answer = []
    cal_list = []
    result = []
    is_equal = False
    aTemp = ""
    cTemp = ""
    for i in quiz:
        for j in i:
            if j == "=":
                is_equal = True
                continue
            if is_equal:
                aTemp += j
            else:
                cTemp += j
        
        is_equal = False
        answer.append(aTemp)
        cal_list.append(cTemp)
        aTemp = ""
        cTemp = ""
    
    # print(cal_list)
    # print(answer)
    for i in range(len(cal_list)):
        if eval(cal_list[i]) == int(answer[i]):
            result.append("O")
        else:
            result.append("X")
    return result