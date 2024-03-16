import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = {}
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    if a not in graph:
        graph[a]=[]
    graph[a].append((b,c))

start, end = map(int, sys.stdin.readline().split())
pq = [(0,start,[start])]
cost = {}
while pq:
    temp, curv,navi = heapq.heappop(pq)
    if curv == end:
        break
    if curv not in cost:
        cost[curv] = temp
        if curv in graph:
            for nextv, nextc in graph[curv]:
                nt = navi + [nextv]
                heapq.heappush(pq,(temp+nextc,nextv,nt))
print(temp)
print(len(navi))
print(*navi)