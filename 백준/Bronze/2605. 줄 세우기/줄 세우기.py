que = []
N = int(input())
order = list(map(int, input().split(" ")))
for i, o in enumerate(order):
    if o == 0:
        que.append(str(i+1))
    else:
        que = que[:-o] + [str(i+1)] + que[-o:]
print(' '.join(que))