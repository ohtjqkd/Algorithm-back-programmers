board = [list(map(int, input().split(" "))) for _ in range(5)]
mapping = {}
bingo = 0
row, col, diag = [5 for _ in range(5)], [5 for _ in range(5)], [5 for _ in range(2)]
for i in range(5):
    for j in range(5):
        mapping[board[i][j]] = (i, j)
is_bingo = False
mc = []
for _ in range(5):
    mc.extend(list(map(int, input().split(" "))))
for i in range(len(mc)):
    r, c = mapping[mc[i]]
    row[r] -= 1
    col[c] -= 1
    if r == c and r + c == 4:
        diag[0] -= 1
        diag[1] -= 1
        if diag[0] <= 0:
            bingo += 1
        if diag[1] <= 0:
            bingo += 1
    elif r == c:
        diag[0] -= 1
        if diag[0] <= 0:
            bingo += 1
    elif r + c == 4:
        diag[1] -= 1
        if diag[1] <= 0:
            bingo += 1
    if row[r] == 0:
        bingo += 1
    if col[c] == 0:
        bingo += 1
    if bingo >= 3:
        print(i+1)
        break