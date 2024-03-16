import sys
from collections import deque

u, d = map(int, sys.stdin.readline().split())
up = {}
for i in range(u):
    a,b = map(int,sys.stdin.readline().split())
    up[a] =b
down = {}
for i in range(d):
    a, b = map(int, sys.stdin.readline().split())
    down[a] = b
queue = deque()
visited= {1:True}
queue.append((1,0))
while queue:
    temp, cnt = queue.popleft()
    if temp == 100:
        print(cnt)
        break

    for i in range(6):
        dice =temp+1+i
        if dice not in visited:
            if dice in up:
                queue.append((up[dice],cnt+1))
                visited[up[dice]] =True
            elif dice in down:
                queue.append((down[dice], cnt+1))
                visited[down[dice]] = True
            else:
                queue.append((temp+1+i,cnt+1))
            visited[dice] =True
