N = int(input())
M = int(input())
nums = list(map(int, input().split(" ")))
dic = {m:True for m in nums}
ret = 0
for n in nums:
    check = dic.get(n)
    if check == True:
        dic[n] = False
        if dic.get(M-n) == True:
            dic[M-n] = False
            ret += 1
print(ret)