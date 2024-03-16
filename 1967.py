import sys
from collections import deque

n = int(sys.stdin.readline())
tree = {}
for i in range(n):
    tree[i+1] = []
for _ in range(n-1):
    a,b,c = map(int,sys.stdin.readline().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
queue = deque()
queue.append((1,0))
maxx=0
maxNode=0
visited = {1:True}
while queue:
    curv ,temp = queue.popleft()
    if maxx < temp:
        maxx =temp
        maxNode = curv
    if curv in tree:
        for next, far in tree[curv]:
            if next not in visited:
                queue.append((next,temp+far))
                visited[next] =True

queue = deque()
queue.append((maxNode,0))
maxx=0
visited = {maxNode:True}
while queue:
    curv ,temp = queue.popleft()
    maxx = max(maxx, temp)
    if curv in tree:
        for next, far in tree[curv]:
            if next not in visited:
                queue.append((next,temp+far))
                visited[next] =True
print(maxx)