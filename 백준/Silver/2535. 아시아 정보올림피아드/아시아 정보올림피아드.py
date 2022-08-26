N = int(input())
nat, print_cnt = [0 for _ in range(N+1)], 0
tables = [list(map(int, input().split(" "))) for _ in range(N)]
tables.sort(key=lambda x: x[2])
while print_cnt < 3:
    a, b, _ = tables.pop()
    if nat[a] >= 2:
        continue
    print(a, b)
    nat[a] += 1
    print_cnt += 1
