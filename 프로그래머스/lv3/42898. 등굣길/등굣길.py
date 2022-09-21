def solution(m, n, puddles):
    answer = [[0] * n for _ in range(m)]
    answer[0][0] = 1
    S = set()
    for p in puddles:
        if len(p) == 0: continue
        S.add((p[0], p[1]))
    for i in range(m):
        for j in range(n):
            if (i+1, j+1) in S or (i + j) == 0:
                continue
            else:
                answer[i][j] = (answer[max(0, i-1)][j] + answer[i][max(0, j-1)]) % 1000000007
    return answer[m-1][n-1] % 1000000007