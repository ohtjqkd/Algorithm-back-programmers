r,c = map(int, input().split())
alphabet = []
for _ in range(r):
    alphabet.append(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    global result
    
    q = set()
    q.add((x,y, alphabet[x][y]))
    
    while q:
        x, y, step = q.pop()
        result = max(result, len(step))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx and nx < r and 0 <= ny and ny < c and alphabet[nx][ny] not in step):
                q.add((nx,ny,step+alphabet[nx][ny]))
                
result = 0
bfs(0,0)
print(result)