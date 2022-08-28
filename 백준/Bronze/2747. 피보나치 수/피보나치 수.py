n = int(input())

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1, f2 = 0, 1
    for _ in range(n-1):
        f1, f2 = f2, f1+f2
    return f2
print(fibo(n))