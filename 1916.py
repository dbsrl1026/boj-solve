import heapq
import sys

n = int(sys.stdin.readline())
bus = int(sys.stdin.readline())
graph ={}
for i in range(1, n+1):
    graph[i] =[]
for _ in range(bus):
    s,e,t = map(int, sys.stdin.readline().split())
    graph[s].append((e,t))
start, end =map(int, sys.stdin.readline().split())
qp = []
qp.append((0,start))
cost = {}
while qp:
    temp, curv = heapq.heappop(qp)
    if curv == end:
        break
    if curv not in cost:
        cost[curv] = temp
        for next, far in graph[curv]:
            heapq.heappush(qp,(far+temp,next))
print(temp)