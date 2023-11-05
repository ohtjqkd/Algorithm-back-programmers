small_height = [int(input()) for _ in range(9)]
small_height.sort()
visited = set()
def dfs(rest, idx, visited: set):
    if (len(visited) == 7):
        if rest == 0:
            return visited
        return
    for i in range(idx + 1, 9):
        if rest - small_height[i] < 0:
            break
        else:
            visited.add(small_height[i])
            ret = dfs(rest - small_height[i], i, visited)
            if (ret):
                return ret
            visited.remove(small_height[i])
ret = sorted(list(dfs(100, -1, visited)))
for r in ret:
    print(r)