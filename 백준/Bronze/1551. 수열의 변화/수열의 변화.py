N, K = tuple(map(int, input().split(" ")))
A = list(map(int, input().split(",")))
for _ in range(K):
    A = [A[i]-A[i-1] for i in range(1, len(A))]
print(','.join(list(map(str, A))))