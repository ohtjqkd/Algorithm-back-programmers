board = [list(map(int, input().split(" "))) for _ in range(9)]
max_value, max_loc = 0, [0, 0]
for i in range(9):
    for j in range(9):
        if board[i][j] >= max_value:
            max_value = board[i][j]
            max_loc = [i, j]

print(max_value)
print(max_loc[0]+1, max_loc[1]+1)