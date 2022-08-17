n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)] 
k = int(input())
locations = [list(map(int, input().split())) for i in range(k)]


##단순구현 시간복잡도에 걸림
# def sum_section(i,j,x,y):
#     sums = 0
#     i,j,x,y = i-1,j-1,x-1,y-1
#     for a in range(i,x+1):
#         for b in range(j,y+1):
#             sums+=board[a][b]
#     return sums

# for i,j,x,y in locations:
#     print(sum_section(i,j,x,y))

##누적합
ac = [[0]*(m+1) for _ in range(n+1)]
ac[1][1] = board[0][0]

for i in range(1,n+1):
    for j in range(1,m+1):
        ac[i][j] = ac[i-1][j] + ac[i][j-1] + board[i-1][j-1] - ac[i-1][j-1]

for i,j,x,y in locations:
    ans = ac[x][y] - ac[i-1][y] - ac[x][j-1] + ac[i-1][j-1]
    print(ans)
