from collections import defaultdict
result = 0
cand = defaultdict(list)
n = int(input())
nums = list(map(int, input().split(" ")))
for idx, n in enumerate(nums):
    cand[n].append(idx)
cand_perm = []
li = sorted(list(cand.items()))
for i in range(len(li)):
    if li[i][0] == 0:
        continue
    for j in range(i + 1, len(li)):
        if li[j][0] == 0:
            continue
        cand_perm.append((li[i][0], li[j][0]))
if cand.get(0):
    for k, value in li:
        if k == 0:
            continue
        if len(value) > 1:
            cand_perm.append((0, k))
if len(cand.get(0, [])) > 2:
    cand_perm.append((0, 0))
possible = set()
for a, b in cand_perm:
    possible.add(a + b)
for p in possible:
    result += len(cand.get(p, []))
print(result)