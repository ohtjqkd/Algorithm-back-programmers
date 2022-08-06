l1, l2 = list(map(lambda x: int(x)-1, input().split(" ")))
print(abs(l1%4-l2%4) + abs(l1//4-l2//4))