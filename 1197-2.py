import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

v, e = map(int, input().split())

graph = defaultdict(list)

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

union = []
sum_w = 0
pq = [(0,1)]
while pq:
    cur_cost, cur_v = heapq.heappop(pq)
    if cur_v not in union:
        union.append(cur_v)
        sum_w += cur_cost
        for next_v, next_cost in graph[cur_v]:
            if next_v not in union:
                heapq.heappush(pq, (next_cost, next_v))
print(sum_w)
