import sys

n,m = map(int,sys.stdin.readline().split())
def dfs(k, cnt,arr):
    if cnt == 0:
        print(*arr)
        return
    for i in range(k, n+1):
        arr.append(i)
        dfs(i, cnt - 1, arr)
        arr.pop()


for i in range(1,n+1):
    dfs(i,m-1,[i])