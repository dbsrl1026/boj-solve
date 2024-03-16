import sys
inf = 100000000
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[inf]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    arr[a-1][b-1] = min(arr[a-1][b-1],c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j != k:
                arr[j][k] = min(arr[j][k], arr[j][i]+arr[i][k])
for i in range(n):
    for j in range(n):
        if arr[i][j] == inf:
            arr[i][j] = 0
for i in range(n):
    print(*arr[i])