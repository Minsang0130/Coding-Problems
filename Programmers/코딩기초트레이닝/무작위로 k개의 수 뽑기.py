def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
    if len(answer) >= k:
        return answer[:k]
    else:
        return answer[:k] + [-1] * (k - len(answer))