import sys

n,m = map(int,sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
def dfs(k,cnt,arr):
    if cnt == 0:
        print(*arr)
        return
    for i in range(k,n):
        arr.append(num[i])
        dfs(i, cnt - 1, arr)
        arr.pop()


for i in range(n):
    dfs(i,m-1,[num[i]])