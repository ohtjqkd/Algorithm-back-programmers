coins = [25, 10, 5, 1]
for _ in range(int(input())):
    t = int(input())
    for i in range(4):
        print(t // coins[i], end=" ")
        t %= coins[i]
    print()