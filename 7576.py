import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
arr = []
queue = deque()
for i in range(m):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if arr[i][j] == 1:
            queue.append((i,j))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while queue:
    x,y = queue.popleft()
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if tx>=0 and tx<m and ty>=0 and ty <n and arr[tx][ty] == 0:
            queue.append((tx,ty))
            arr[tx][ty] = arr[x][y]+1
if any(0 in l for l in arr):
    print(-1)
else:
    a = max(map(max, arr)) -1
    print(a)