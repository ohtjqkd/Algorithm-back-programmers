import sys

def solution(maps):
    answer = []
    global M
    M = list(map(list, maps))
    row, col = len(maps), len(maps[0])
    def check_area(x, y):
        ret = 0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        stack = [[x, y]]
        while stack:
            x, y = stack.pop()
            if M[x][y] == 'X':
                continue
            ret += int(M[x][y])
            M[x][y] = 'X'
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 > xx or xx >= row or 0 > yy or yy >= col or M[xx][yy] == 'X':
                    continue
                stack.append([xx, yy])
        return ret
    
    for i in range(row):
        for j in range(col):
            if M[i][j] == 'X':
                continue
            answer.append(check_area(i, j))
    if not answer:
        answer.append(-1)
    return sorted(answer)