P = 1_000_000_007

def factorial(n):
    ret = 1
    for i in range(n, 1, -1):
        ret = (ret * i) % P
    return ret
        
def pow(base, exp):
    ret = 1
    while exp > 0:
        if exp % 2 == 1:
            ret *= base
            ret %= P
        base = (base * base) % P
        exp //= 2
    return ret

N, K = map(int, input().split(" "))

denom = factorial(K) * factorial(N-K) % P
print(factorial(N) * pow(denom, P - 2) % P)

