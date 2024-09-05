import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 오름차순 정렬 후 앞 5개 숫자 저장
    arr.sort()
    big_num = arr[:5]

    # 내림차순 정렬 후 앞 5개 숫자 저장
    arr.sort(reverse=True)
    small_num = arr[:5]

    result = []
    for i in range(5):
        result.append(small_num[i])
        result.append(big_num[i])

    print(f'#{test_case} {" ".join(map(str, result))}')