def z(N, r, c):
    if N == 1:
        if (r, c) == (0, 0):
            return 0
        elif (r, c) == (0, 1):
            return 1
        elif (r, c) == (1, 0):
            return 2
        elif (r, c) == (1, 1):
            return 3
    sqrt = 2 ** (N-1)
    if sqrt > r:
        if sqrt > c:
            return z(N-1, r, c)
        elif sqrt <= c:
            return sqrt ** 2 + z(N-1, r, c-sqrt)
    
    elif sqrt <= r:
        if sqrt > c:
            return sqrt ** 2 * 2 + z(N-1, r-sqrt, c)
        elif sqrt <= c:
            return sqrt ** 2 * 3 + z(N-1, r-sqrt, c-sqrt)
        

N, r, c = list(map(int, input().split(' ')))

print(z(N, r, c))
