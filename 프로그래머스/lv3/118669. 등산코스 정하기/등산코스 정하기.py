from heapq import heappush, heappop
from collections import defaultdict
def solution(n, paths, gates, summits):
    dp = [float('inf') for _ in range(n+1)]

    edges = defaultdict(list)
    for i, j, w in paths:
        edges[i].append((j, w))
        edges[j].append((i, w))
    heap = [(0, gate) for gate in gates]
    while heap:
        curr_intensity, node = heappop(heap)
        if dp[node] <= curr_intensity:
            continue
        dp[node] = curr_intensity
        if node in summits:
            continue
        for next_node, next_weight in edges[node]:
            intensity = max(curr_intensity, next_weight)
            if dp[next_node] <= intensity:
                continue
            heappush(heap, (intensity, next_node))
    answer = [[s, dp[s]] for s in summits]
    answer.sort(key=lambda x: (x[1], x[0]))
    return answer[0]
        
    

# from heapq import heappush, heappop
# import sys
# sys.setrecursionlimit = 1000000000
# def solution(n, paths, gates, summits):
#     answer = []
#     to_summit = [i for i in range(n + 1)]
#     to_gate = [i for i in range(n + 1)]
#     def find(node, to, tmp = 200):
#         if node != to[node]:
#             to[node] = find(to[node], to)
#         return to[node]
#     def union(a, b, to, is_in):
#         if b in is_in:
#             return to
#         to[b] = a
#         return to
#     is_summit = set(summits)
#     is_gate = set(gates)
#     heap = []
#     for a, b, w in paths:
#         heappush(heap, (w, a, b))
#     while heap:
#         w, a, b = heappop(heap)
#         to_gate_a, to_summit_a = find(a, to_gate), find(a, to_summit)
#         to_gate_b, to_summit_b = find(b, to_gate), find(b, to_summit)
#         if to_gate_a in is_gate and to_summit_b in is_summit:
#             answer.append([to_summit_b, w])
#         if to_gate_b in is_gate and to_summit_a in is_summit:
#             answer.append([to_summit_a, w])
#         if to_gate_a in is_gate:
#             to_gate = union(a, b, to_gate, is_gate)
#         else:
#             to_gate = union(b, a, to_gate, is_gate)
#         if to_summit_a in is_summit and to_summit_b in is_summit:
#             if to_summit_a > to_summit_b:
#                 to_summit = union(b, a, to_summit, is_summit)
#             else:
#                 to_summit = union(a, b, to_summit, is_summit)
#         elif to_summit_a in is_summit:
#             to_summit = union(a, b, to_summit, is_summit)
#         else:
#             to_summit = union(b, a, to_summit, is_summit)
    
#     answer.sort(key=lambda x: (x[1], x[0]))
#     return answer[0]
