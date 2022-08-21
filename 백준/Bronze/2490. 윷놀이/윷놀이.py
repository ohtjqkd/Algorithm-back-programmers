from collections import Counter
p = "EABCD"
yuts = [Counter(list(map(int, input().split(" ")))) for _ in range(3)]
for y in yuts:
    print(p[y.get(0, 0)])