import sys
from collections import deque

n = int(sys.stdin.readline())
dic = {}
for i in range(1,n+1):
    dic[i] = []
l = int(sys.stdin.readline())
for i in range(l):
    x, y = map(int,sys.stdin.readline().split())
    dic[x].append(y)
    dic[y].append(x)
visited = []
queue = deque()
queue.append(1)
while queue:
    temp = queue.popleft()
    if temp in visited:
        continue
    visited.append(temp)
    queue.extend(dic[temp])
print(len(visited)-1)