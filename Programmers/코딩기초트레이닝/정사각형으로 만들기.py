def solution(arr):
    # 배열의 크기가 같으면 그대로 반환
    if len(arr) == len(arr[0]):
        return arr

    elif len(arr) > len(arr[0]):
        for i in range(len(arr)):
            while len(arr[i]) != len(arr):
                arr[i].append(0)

    else:
        for _ in range(len(arr[0]) - len(arr)):
            arr.append([0] * len(arr[0]))

    return arr


print(solution([[[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]]))