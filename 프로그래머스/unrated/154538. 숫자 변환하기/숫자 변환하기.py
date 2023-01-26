def solution(x, y, n):
    answer = 0
    mem = [float('inf') for _ in range(y * 3 + 1)]
    mem[x] = 0
    for i in range(x, y + 1):
        if mem[i] == float('inf'):
            continue
        if mem[i] + 1 < mem[i + n]:
            mem[i + n] = mem[i] + 1
        if mem[i] + 1 < mem[i * 2]:
            mem[i * 2] = mem[i] + 1
        if mem[i] + 1 < mem[i * 3]:
            mem[i * 3] = mem[i] + 1
        if i == y:
            break
    
    return mem[y] if mem[y] != float('inf') else -1