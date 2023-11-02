X = int(input())

dp = [0 for _ in range(X+1)]

for i in range(2, len(dp)):
    m = dp[i-1]
    t = dp[i//2] if i % 2 == 0 else float('inf')
    th = dp[i//3] if i % 3 == 0 else float('inf')
    dp[i] = min(m, t, th)+1
print(dp[-1])