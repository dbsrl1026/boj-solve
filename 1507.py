n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))
answer = [[True]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(i+1,n):
            if k == i or k == j:
                continue
            if grid[i][j] > grid[i][k] + grid[k][j]:
                print(-1)
                exit(0)
            if grid[i][j] == grid[i][k] + grid[k][j]:
                answer[i][j] = False

result = 0
for i in range(n):
    for j in range(1+i,n):
        if answer[i][j]:
            result += grid[i][j]
print(result)
