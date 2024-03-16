import heapq
import sys


def dijikstra(graph, start, end):
    pq = []
    cost = {}
    heapq.heappush(pq,(0,start))
    while pq:
        temp, curv = heapq.heappop(pq)
        if curv == end:
            return temp
        if curv not in cost:
            cost[curv] = temp
            for next, far in graph[curv]:
                heapq.heappush(pq,(temp+far,next))
    print(-1)
    exit()

n, e = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, n + 1):
    graph[i] = []
for _ in range(e):
    a, b, d = map(int, sys.stdin.readline().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
u, v = map(int, sys.stdin.readline().split())

uTOv = dijikstra(graph,u,v)
oneTOu = dijikstra(graph,1,u)
oneTOv = dijikstra(graph,1,v)
nTOu = dijikstra(graph,n,u)
nTOv = dijikstra(graph,n,v)
case=[]
case.append(oneTOu+uTOv+nTOv)
case.append(oneTOv+uTOv+nTOu)
case.append(oneTOu+nTOu+uTOv*2)
case.append(oneTOv+nTOv+uTOv*2)
print(min(case))