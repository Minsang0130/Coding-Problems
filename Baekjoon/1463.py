def solution(N):
    num_list = [0] * (N + 1)
    
    for i in range(2, N + 1):
        num_list[i] = num_list[i - 1] + 1
        if i % 2 == 0:
            num_list[i] = min(num_list[i], num_list[i // 2 ] + 1)
        if i % 3 == 0:
            num_list[i] = min(num_list[i], num_list[i // 3] + 1)
    
    return num_list[N]

def main():
    N = int(input())
    print(solution(N))

if __name__ == "__main__":
    main()