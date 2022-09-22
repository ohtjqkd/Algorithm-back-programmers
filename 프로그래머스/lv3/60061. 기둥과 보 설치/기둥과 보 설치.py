def solution(n, build_frame):
    def check_pillar(x, y):
        if y == 0:
            return True
        if pillar[x][y - 1] == 1:
            return True
        elif bar[x - 1][y] == 1 or bar[x][y] == 1:
            return True
        return False
    
    def check_bar(x, y):
        if y > 0 and (pillar[x][y-1] or pillar[x+1][y-1]):
            return True
        if x > 0 and bar[x-1][y] and bar[x+1][y]:
            return True
        return False
    
    def can_delete(x, y):
        for xx in range(x - 1, x + 2):
            for yy in range(y, y + 2):
            # xx, yy = x + dx[i], y + dy[i]
                # if 0 < xx and 0 < yy:
                if bar[xx][yy] == 1 and not check_bar(xx, yy):
                    return False
                if pillar[xx][yy] == 1 and not check_pillar(xx, yy):
                    return False
        return True
    
    pillar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    bar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    
    for x, y, kind, cmd in build_frame:
        if kind == 0:
            if cmd == 1:
                if check_pillar(x, y):
                    pillar[x][y] = 1
            else:
                pillar[x][y] = 0
                if not can_delete(x, y):
                    pillar[x][y] = 1
        else:
            if cmd == 1:
                if check_bar(x, y):
                    bar[x][y] = 1
            else:
                bar[x][y] = 0
                if not can_delete(x, y):
                    bar[x][y] = 1
    def print_b(board):
        for b in board:
            print(b)
    ret = []
    for i in range(n + 1):
        for j in range(n + 1):
            if pillar[i][j] == 1:
                ret.append([i, j, 0])
            if bar[i][j] == 1:
                ret.append([i, j, 1])
    ret.sort()
    return ret
                    

    


    
    
    
    