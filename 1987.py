import sys


r,c = map(int,sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
maxx = 0
def dfs(x,y,visited,cnt):
    global maxx
    maxx = max(maxx, cnt)
    for i in range(4):
        tx,ty =x + dx[i], y + dy[i]
        if 0 <= tx < r and 0 <= ty <c and not arr[tx][ty] in visited:
            visited[arr[tx][ty]] =True
            dfs(tx,ty,visited,cnt+1)
            visited.pop(arr[tx][ty])

dfs(0,0,{arr[0][0]:True},1)
print(maxx)

