import sys

input = sys.stdin.readline

# 시간초과 solution T _ T but pypy3에서는 느리지만 통과
def solution():
    N = int(input())
    pages = list(map(int, input().split(" ")))
    S = [[pages[i] if i == j else 0 for i in range(N)] for j in range(N)]
    dp = [[0 if i == j else float('inf') for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            # if j - i == 1:
                # dp[i][j] = dp[i][j - 1] + dp[i + 1][j]
            S[i][j] = S[i][j - 1] + S[j][j]

    for i in range(1, N):
        for j in range(N - i):
            for k in range(i):
                r = dp[j][j + k]
                c = dp[j + k + 1][i + j]
                dp[j][i + j] = min(dp[j][i + j], r + c + S[j][i + j])

    print(dp[0][N - 1])

T = int(input())

for _ in range(T):
    solution()