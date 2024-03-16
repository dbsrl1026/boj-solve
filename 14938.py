import heapq
import sys

n,m,r = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))
graph = {}
for i in range(1,1+n):
    graph[i] = []
for _ in range(r):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

maxx = 0
for i in range(1,n+1):
    farm = 0
    pq = []
    costs = {}
    heapq.heappush(pq,(0,i))
    while pq:
        curc, curv = heapq.heappop(pq)
        if curc <= m and curv not in costs:
            farm += item[curv-1]
            costs[curv] = curc
            for nextc, nextv in graph[curv]:
                heapq.heappush(pq, (nextc+curc, nextv))
    maxx = max(maxx, farm)

print(maxx)