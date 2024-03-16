def dfs(grid, x, y,m,n, visited):
    if grid[x][y] == '0' or visited[x][y] == '1':
        return 0
    visited[x][y]='1'
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        if x+dx[i]<0 or x+dx[i]>=m or y+dy[i]<0 or y+dy[i] >=n:
            continue
        dfs(grid,x+dx[i],y+dy[i],m,n,visited)
    return 1



grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]

num = 0
m = 4;
n = 5
visited = [['0' for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        num += dfs(grid, i, j,m, n,visited)
print(num)
print(visited)
