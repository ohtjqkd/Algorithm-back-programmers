from collections import deque

N = int(input())
target = deque([])
for i in range(N):
    target.appendleft(int(input()))
stack, result = [], []

for i in range(1, N + 1):
    stack.append(i)
    result.append("+")
    while stack and stack[-1] == target[-1]:
        stack.pop(), target.pop()
        result.append("-")
if len(target) > 0:
    print("NO")
else:
    for sign in result:
        print(sign)