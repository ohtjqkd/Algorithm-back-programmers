l, c = map(int, input().split())
s = list(input().split())

vowel = ['a','e','i','o','u']

s.sort()

def password():
    q = list()
    visited = list()
    result = list()
    for i in s:
        if i in vowel:
            q.append((i,1,0))
        else:
            q.append((i,0,1))
    while q:
        prev, v, c = q.pop(0)
        if len(prev) == l:
            if v > 0 and c > 1:
                result.append(prev)
            else:
                continue
        visited.append(prev)
        for j in s:
            if j in prev:
                continue
            if prev[-1] > j:
                continue
            if j in vowel:
                q.append((prev+j,v+1,c))
            else:
                q.append((prev+j,v,c+1))

    return result
answer = password()
answer.sort()
for o in answer:
    print(o)