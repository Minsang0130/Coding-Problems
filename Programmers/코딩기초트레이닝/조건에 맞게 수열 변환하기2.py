def solution(arr):
    count = 0
    while True:
        # temp_list를 새로 초기화
        temp_list = []
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                temp_list.append(arr[i] // 2)
            elif arr[i] < 50 and arr[i] % 2 != 0:
                temp_list.append(arr[i] * 2 + 1)
            else:
                temp_list.append(arr[i])

        # arr와 temp_list가 동일한지 체크
        if arr == temp_list:
            return count
        else:
            arr = temp_list[:]  # temp_list의 값을 arr에 복사
            count += 1