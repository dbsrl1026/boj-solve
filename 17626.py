import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
queue.append((n,0))
visited = {n:True}
while queue:
    temp, cnt = queue.popleft()
    if temp == 0:
        print(cnt)
        break
    max = int(temp**0.5)
    for i in range(max,0,-1):
        if temp - i**2 not in visited:
            queue.append((temp-i**2, cnt+1))
            visited[temp-i**2] = True

