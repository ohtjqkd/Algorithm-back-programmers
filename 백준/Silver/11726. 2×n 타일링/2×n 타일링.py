# 2xN 타일링

N = int(input())
dp = [0] * max(N, 2)
dp[0], dp[1] = 1, 2

for i in range(2, len(dp)):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
print(dp[N - 1])