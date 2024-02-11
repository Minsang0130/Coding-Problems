def solution(arr, queries):
    answer = []
    result = []
    num = 0
    for a, b, c in queries:
        for i in range(a,b+1):
            if arr[i] > c :
              answer.append(arr[i])
        if i ==b and len(answer) != 0:
          answer.sort()
          result.append(answer[0])
          answer.clear()
        else:
          result.append(-1)
    return result
