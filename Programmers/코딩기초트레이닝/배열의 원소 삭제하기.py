def solution(arr, delete_list):
    for num in delete_list:
        if num in arr:
            del arr[arr.index(num)]
    return arr