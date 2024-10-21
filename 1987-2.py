import sys
input = sys.stdin.readline
r, c = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(list(input().rstrip()))


def dfs(x, y, cnt, visited):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = []
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < r and 0 <= next_y < c and grid[next_x][next_y] not in visited:
            visited[grid[next_x][next_y]] = True
            answer.append(dfs(next_x, next_y, cnt + 1, visited))
            visited.pop(grid[next_x][next_y])
    if len(answer) == 0:
        return cnt
    else:
        return max(answer)
print(dfs(0, 0, 1, {grid[0][0] : True}))
