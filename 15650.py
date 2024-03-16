import sys

n,m = map(int,sys.stdin.readline().split())
def dfs(k, cnt,arr):
    if cnt == 0:
        print(*arr)
        return
    for i in range(k+1, n-cnt+2):
        arr.append(i)
        dfs(i, cnt - 1, arr)
        arr.pop()


for i in range(1,n-m+2):
    dfs(i,m-1,[i])