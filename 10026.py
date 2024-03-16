import sys
from collections import deque


def bfs(arr,n):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    queue = deque()
    visited = {}
    cnt = 0
    for i in range(n):
        for j in range(n):
            if (i,j) not in visited:
                cnt+=1
                queue.append((i,j))
                visited[(i,j)] = True
                curC = arr[i][j]
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        tx = x+dx[k]
                        ty = y+dy[k]
                        if tx>= 0 and tx< n and ty>=0 and ty<n and (tx,ty) not in visited and arr[tx][ty] == curC:
                            queue.append((tx,ty))
                            visited[(tx,ty)] = True
    return cnt

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
normal = bfs(arr,n)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
handi = bfs(arr,n)
print(normal,handi)