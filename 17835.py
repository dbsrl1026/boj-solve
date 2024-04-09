import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n, m ,k = map(int, input().split())
load = defaultdict(list)
for _ in range(m):
    a,b,d = map(int, input().split())
    load[b].append((a,d))
points = list(map(int, input().split()))

distance = [100000000000000] * n
heap = []
for point in points:
    heapq.heappush(heap,(0,point))

while heap:
    d, point = heapq.heappop(heap)
    if d < distance[point-1]:
        distance[point-1] = d
        for next_point, cost in load[point]:
            next_cost = d + cost
            heapq.heappush(heap,(next_cost,next_point))

max_d = max(distance)
max_k = distance.index(max_d)+1
print(max_k)
print(max_d)
