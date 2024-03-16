import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def checkIsland():
    queue = deque()
    visited = {(0,0):True}
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if 0<=tx<n and 0<= ty<m and (tx,ty) not in visited and arr[tx][ty] !=1:
                queue.append((tx,ty))
                visited[(tx,ty)] =True
                arr[tx][ty] = -1
def melt():
    switch = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                switch =1
                tempcnt = 0
                for k in range(4):
                    tx = i+dx[k]
                    ty = j+dy[k]
                    if 0 <= tx < n and 0 <= ty < m and arr[tx][ty] == -1:
                        tempcnt+=1
                if tempcnt >=2:
                    arr[i][j] = 0
    return switch

arr[0][0] = -1
cnt = 0
while True:
    checkIsland()
    if melt() == -1:
        print(cnt)
        exit()
    else:
        cnt+=1

