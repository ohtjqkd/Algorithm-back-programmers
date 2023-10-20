N, K = input().split(' ')
array = []

array = list(map(int, input().split(' ')))
    
array = sorted(array)

idx = int(K) - 1

print(array[idx])

