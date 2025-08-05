def solution(answers):
    # 수포자 별 정답일때 카운트 할 변수
    count1 = 0
    count2 = 0
    count3 = 0
    
    # 수포자별 찍은 번호
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
     
    for idx, ans in enumerate(answers):
        if ans == answer1[idx % len(answer1)]:
            count1 += 1
        if ans == answer2[idx % len(answer2)]:
            count2 += 1
        if ans == answer3[idx % len(answer3)]:
            count3 += 1
    
    max_num = max(count1, count2, count3)
    result = [idx+1 for idx, num in enumerate([count1, count2, count3]) if num == max_num]
    return result