import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    temp = sys.stdin.readline()
    graph.append(temp[:-1])

visit = [[False for x in range(m)]for x in range(n)]
dp = [[0 for x in range(m)]for x in range(n)]
def dfs(x, y, dist):
    global maxdist
    maxdist = max(maxdist, dist)
    move = int(graph[x][y])
    adjlist = [[x-move, y], [x+move, y], [x, y-move], [x, y+move]]
    for point in adjlist:
        nx=point[0]
        ny=point[1]
        if nx >=0 and nx<n and ny >= 0 and ny < m and graph[nx][ny] != 'H' and dist + 1>dp[nx][ny]:
            if visit[nx][ny] == False:
                dp[nx][ny] = dist + 1
                visit[nx][ny]=True
                dfs(nx, ny, dist+1)
                visit[nx][ny]=False
            else:
                print(-1)
                exit()

global maxdist
maxdist = -1
dfs(0, 0, 1)
print(maxdist)