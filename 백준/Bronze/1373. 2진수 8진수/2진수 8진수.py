b = list(input())
ret =[]
b.reverse()
for i in range(0, len(b), 3):
    t = b[i:min(i+3, len(b))]
    s = 0
    for j in range(len(t)):
        if t[j] == '1':
            s += 2**j
    ret.append(str(s))
print(''.join(reversed(ret)))