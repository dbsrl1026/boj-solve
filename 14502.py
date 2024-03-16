import copy
import sys
from collections import deque


def bfs(x1,x2,x3,y1,y2,y3,arrr,n,m):
    arrr[x1][y1] = 1
    arrr[x2][y2] = 1
    arrr[x3][y3] = 1
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited ={}
    for i in range(n):
        for j in range(m):
            if arrr[i][j] == 2 and (i,j) not in visited:
                queue = deque()
                queue.append((i,j))
                visited[(i,j)] = True
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        tx = x+dx[k]
                        ty = y+dy[k]
                        if 0<=tx<n and 0<= ty < m and arrr[tx][ty] == 0:
                            queue.append((tx,ty))
                            arrr[tx][ty] = 2
                            visited[(tx,ty)] = True
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arrr[i][j] == 0:
                cnt+= 1
    return cnt

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
maxx = 0
for i in range(n * m):
    x1 = i // m
    y1 = i % m
    if arr[x1][y1] != 0:
        continue
    for j in range(i + 1, n * m):
        x2 = j // m
        y2 = j % m
        if arr[x2][y2] != 0:
            continue
        for k in range(j + 1, n * m):
            x3 = k // m
            y3 = k % m
            if arr[x3][y3] != 0:
                continue
            arrr = copy.deepcopy(arr)
            safe = bfs(x1,x2,x3,y1,y2,y3,arrr,n,m)
            maxx = max(maxx, safe)
print(maxx)