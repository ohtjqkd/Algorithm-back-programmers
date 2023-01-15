N = input()
S = "1"*len(N)
ret = len(N) if int(N) >= int(S) or int(N) == 0 else len(N)-1
print(ret)