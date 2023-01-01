def atOper(A, B):
    return (A+B)*(A-B)

A, B = map(int, input().split(" "))
print(atOper(A, B))