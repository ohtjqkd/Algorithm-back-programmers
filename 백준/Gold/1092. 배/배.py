##problem 1092

n = int(input())
crains = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
result = 0
crains.sort(reverse=True)
boxes.sort(reverse=True)

while boxes:
    if crains[0] < boxes[len(boxes)-1]:
        result = -1
        break
    for i in range(n):
        for j in range(len(boxes)):
            if crains[i] >= boxes[j]:
                del(boxes[j])
                break
    result += 1

print(result)
