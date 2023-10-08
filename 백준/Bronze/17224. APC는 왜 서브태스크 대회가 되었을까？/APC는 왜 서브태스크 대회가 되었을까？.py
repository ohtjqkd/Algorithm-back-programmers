pos = []
result = 0
n, l, k = map(int, input().split())
for i in range(n):
    e, h = map(int,input().split())
    pos.append((e,h))

pos.sort()
pos.sort(key=lambda x:x[1]-l)        
sol = 0
for i in range(len(pos)):
    if pos[i][1] <= l:
        result += 140
        sol += 1
    elif pos[i][0] <= l:
        result += 100
        sol += 1
    if sol >= k:
        break

print(result)