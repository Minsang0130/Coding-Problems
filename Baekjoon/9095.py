def solution(N):
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, 12):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[N]

T = int(input())
def main():
    for test_case in range(1, T+1):
        N = int(input())
        
        print(solution(N))
    
if __name__ == "__main__":
    main()