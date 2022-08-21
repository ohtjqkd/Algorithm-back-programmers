p = 0
max_p = 0
for _ in range(10):
    d, u = map(int, input().split(" "))
    p -= d
    max_p = max(max_p, p)
    p += u
    max_p = max(max_p, p)
print(max_p)

