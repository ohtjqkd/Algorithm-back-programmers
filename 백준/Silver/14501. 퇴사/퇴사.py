D = int(input())
P = [list(map(int, input().split(" "))) for _ in range(D)]
dp = [0 for _ in range(D + 1)]
for i, [d, w] in enumerate(P):
    if i + d > D:
        continue
    if i > 0:
        dp[i] = max(dp[i - 1], dp[i])
    dp[i + d] = max(dp[i + d], dp[i] + w)
print(max(dp))