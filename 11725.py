import sys
from collections import deque

n= int(sys.stdin.readline())
node ={}
for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    if a not in node:
        node[a] = []
    node[a].append(b)
    if b not in node:
        node[b] = []
    node[b].append(a)


root = {}
queue = deque()
visited = {1:True}
queue.append(1)
while queue:
    temp = queue.popleft()
    for v in node[temp]:
        if v not in visited:
            queue.append(v)
            visited[v] =True
            root[v] = temp
root = dict(sorted(root.items()))
for k in root.values():
    print(k)