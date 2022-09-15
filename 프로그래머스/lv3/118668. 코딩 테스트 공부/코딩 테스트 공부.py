def solution(alp, cop, problems):
    req_a, req_c = max(problems, key = lambda x: x[0])[0], max(problems, key = lambda x: x[1])[1]
    dp = [[float('inf') for _ in range(req_a + 1)] for _ in range(req_c + 1)]
    alp, cop = min(alp, req_a), min(cop, req_c)
    for i in range(alp + 1):
        for j in range(cop + 1):
            dp[j][i] = 0
    for i in range(cop, req_c + 1):
        for j in range(alp, req_a + 1):
            if i < req_c:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if j < req_a:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            for ar, cr, ad, cd, co in problems:
                if ar <= j and cr <= i:
                    next_j, next_i = min(req_a, j + ad), min(req_c, i + cd)
                    dp[next_i][next_j] = min(dp[i][j] + co, dp[next_i][next_j])
    return dp[-1][-1]