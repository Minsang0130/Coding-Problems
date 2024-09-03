import sys
sys.stdin = open('sample_input(2).txt', 'r')

def solution(nums):
    length = len(nums)
    lis = [1] * length
    prev = [-1] * length
    
    for i in range(1, length):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[i] + 1
                prev[i] = j
    
    maxnum = max(lis)
    # print(maxnum)
    maxindex = lis.index(maxnum)
    # print(maxindex)
    result = []
    while maxindex != -1:
        result.append(nums[maxindex])
        maxindex = prev[maxindex]
    return len(result)

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    print(f'#{test_case} {solution(arr)}')