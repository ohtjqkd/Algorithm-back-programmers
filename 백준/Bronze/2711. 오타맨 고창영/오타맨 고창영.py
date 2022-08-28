for _ in range(int(input())):
    t, s = input().split(" ")
    s = list(s)
    del(s[int(t)-1])
    print(''.join(s))