from collections import defaultdict
import heapq

v, e = map(int, input().split())
start = int(input())
graph = defaultdict(list)

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

pq = [(0,start)]
cost = {}

while pq:
    cur_cost, cur_v = heapq.heappop(pq)
    if cur_v not in cost:
        cost[cur_v] = cur_cost
        for next_v, next_cost in graph[cur_v]:
            heapq.heappush(pq,(cur_cost+next_cost, next_v))

for i in range(1, v+1):
    if i in cost:
        print(cost[i])
    else:
        print("INF")
