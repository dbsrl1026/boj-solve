import copy
import sys

n,m = map(int,sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
visited = []

def dfs(cnt,arr,num):
    if cnt <= 0:
        if arr not in visited:
            temp = copy.deepcopy(arr)
            visited.append(temp)
            print(*arr)
        return
    for i in range(n):
        arr.append(num[i])
        dfs(cnt - 1, arr)
        arr.pop()


for i in range(n):
    dfs(m-1,[num[i]],num)