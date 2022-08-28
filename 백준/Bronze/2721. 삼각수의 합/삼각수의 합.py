for _ in range(int(input())):
    T = int(input())
    S = 0
    dp = [i+1 for i in range(T+1)]
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
        S += dp[i]*i
    print(S)