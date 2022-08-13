##problem 1920
# 1 <= N, M <= 1000000 따라서 O(N*M) 시간복잡도로는 풀 수 없다. O(MlogN)의 알고리즘이 필요 (ex. 이진탐색)

N, A = int(input()), list(map(int, input().split()))
M, B = int(input()), list(map(int, input().split()))

##이진탐색함수 구현
##arr는 대상리스트, b는 타겟값

def is_b(arr, b):
    maxs = len(arr)-1
    mins = 0
    while mins <= maxs:
        mid = (maxs+mins)//2
        if arr[mid] == b:
            return 1
        if arr[mid] > b:
            maxs = mid-1
        else:
            mins = mid+1
    return 0
A.sort()
for i in B:
    print(is_b(A, i))