##test code
# n = 4

n = int(input())
f1 = 1
f2 = 2

for _ in range(n-2):
    tmp = (f1+f2) % 15746
    f1 = f2
    f2 = tmp

if n == 1:
    print(1)
else:
    print(f2)

