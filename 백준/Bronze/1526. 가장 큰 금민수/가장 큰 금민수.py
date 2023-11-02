N = input()

comb = []
stack = ['4', '7'] if int(N) > 7 else ['4']
while stack:
    p = stack.pop()
    # for p in prev:
    for fs in ['4', '7']:
        if int(fs+p) > int(N):
            comb.append(p)
            continue
        stack.append(fs+p)
comb.sort(key=lambda x: int(x))
print(comb[-1])