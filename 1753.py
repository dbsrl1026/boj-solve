import heapq
import sys

v, e = map(int, sys.stdin.readline().split())
graph= {}
start = int(sys.stdin.readline())
for i in range(1, 1+v):
    graph[i] =[]
for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

pq = []
cost = {}
heapq.heappush(pq, (0, start))
while pq:
    temp, curv = heapq.heappop(pq)
    if curv not in cost:
        cost[curv] = temp
        for next, far in graph[curv]:
            heapq.heappush(pq,(temp+far, next))
for i in range(1,v+1):
    if i not in cost:
        print("INF")
    else:
        print(cost[i])