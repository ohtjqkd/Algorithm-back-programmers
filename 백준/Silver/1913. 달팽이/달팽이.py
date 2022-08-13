N = int(input())
T = int(input())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
board = [[0 for _ in range(N)] for _ in range(N)]
dir = 0
curr = (0, 0)
for i in range(N**2):
    x, y = curr
    board[x][y] = str(N**2-i)
    if board[x][y] == str(T):
        T = f'{x+1} {y+1}'
    xx, yy = x+dx[dir], y+dy[dir]
    if xx < 0 or xx >= N or yy < 0 or yy >= N or board[xx][yy] != 0:
        dir = (dir+1) % 4
    curr = (x+dx[dir], y+dy[dir])
for b in board:
    print(' '.join(b))
print(T)