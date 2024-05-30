ck, tmp, ans, S = False,'','',input()

for i in S:
    if i == ' ':
        ans += tmp[::-1] + ' '
        tmp = ''
    elif i == '<':
        ans += tmp[::-1] + '<'
        tmp = ''
        ck = True
    elif i == '>':
        ans += '>'
        ck = False
    else:
        if ck:
            ans += i
        else:
            tmp += i
            
print(ans+tmp[::-1])