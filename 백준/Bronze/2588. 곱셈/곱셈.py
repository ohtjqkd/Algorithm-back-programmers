a = int(input())
b = int(input())

result = a*b

for _ in range(3):
    print(a*(b%10))
    b//=10
print(result)