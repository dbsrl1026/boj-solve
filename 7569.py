import sys
from collections import deque

n,m,h = map(int, sys.stdin.readline().split())
arr = []
queue = deque()
for i in range(h):
    temp = []
    for j in range(m):
        temp.append(list(map(int,sys.stdin.readline().split())))
    arr.append(temp)
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 1:
                queue.append((i,j,k))
dx = [-1,0,1,0,0,0]
dy = [0,-1,0,1,0,0]
dz = [0,0,0,0,1,-1]
while queue:
    x,y,z = queue.popleft()
    for i in range(6):
        tx = x+dx[i]
        ty = y+dy[i]
        tz = z+dz[i]
        if tx>=0 and tx<h and ty>=0 and ty <m and tz >= 0 and tz<n and arr[tx][ty][tz] == 0:
            queue.append((tx,ty,tz))
            arr[tx][ty][tz] = arr[x][y][z]+1

ma = 0
for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            elif arr[i][j][k] > ma:
                ma = arr[i][j][k]
print(ma-1)
