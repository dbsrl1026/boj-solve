import heapq
import sys

n, m, x = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1,n+1):
    graph[i] = []
for _ in range(m):
    a, b, d = map(int, sys.stdin.readline().split())
    graph[a].append((b,d))
timer = []
for i in range(1,n+1):
    go= 0
    come = 0
    if i == x:
        continue
    pq =[]
    heapq.heappush(pq,(0,i))
    visited={}
    while pq:
        dist, curv = heapq.heappop(pq)
        if curv == x:
            go = dist
            break
        if curv not in visited:
            visited[curv] = dist
            for next, far in graph[curv]:
                heapq.heappush(pq,(dist+far,next))
    pq = []
    heapq.heappush(pq, (0, x))
    visited = {}
    while pq:
        dist, curv = heapq.heappop(pq)
        if curv == i:
            come = dist
            break
        if curv not in visited:
            visited[curv] = dist
            for next, far in graph[curv]:
                heapq.heappush(pq,(dist+far,next))
    timer.append(go+come)

print(max(timer))
