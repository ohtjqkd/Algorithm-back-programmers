def rev(s):
    s = str(s)
    ret = 0
    len_s = len(s)
    for i in range(len_s):
        ret += int(s[i]) * (10 ** i)
    return ret

x, y = input().split()
print(rev(rev(x)+rev(y)))