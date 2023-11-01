N, S = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

def comb(arr, n):
    ret = []
    if n > len(arr): return ret
    if n == 1:
        for i in arr:
            ret.append([i])
    elif n > 1:
        for i in range(len(arr)-n+1):
            for temp in comb(arr[i+1:], n-1):
                ret.append([arr[i]]+temp)
    return ret
ret = []
cnt = 0
for i in range(1, N+1):
    ret.extend(comb(arr, i))
for r in ret:
    if sum(r) == S:
        cnt += 1
print(cnt)