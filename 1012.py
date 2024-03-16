import sys
from collections import deque
def bfs(arr,m,n):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited = {}
    queue = deque()
    count = 0
    for i in range(n):
        for j in range(m):
            if (i,j) in visited or arr[i][j] == 0:
                continue
            queue.append((i,j))
            count +=1
            while queue:
                y,x = queue.popleft()
                if (y,x) in visited:
                    continue
                visited[(y,x)] = True
                for k in range(4):
                    newX = x+dx[k]
                    newY = y+dy[k]
                    if newX>= 0 and newX<m and newY>=0 and newY<n and (newY,newX) not in visited and arr[newY][newX] == 1:
                        queue.append((newY,newX))
    return count


testCase = int(sys.stdin.readline())
for _ in range(testCase):
    m,n,k = map(int, sys.stdin.readline().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    print(bfs(arr,m,n))
