##problem 585
pay = int(input())
coins = [500, 100, 50, 10, 5, 1]
result = 0
change = 1000 - pay

for i in coins:
    while change-i >= 0:
        change -= i
        result += 1
    if change == 0:
        break
        
print(result)