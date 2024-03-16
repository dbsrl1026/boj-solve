import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][k]==0 and arr[j][i] != 0 and arr[i][k] != 0:
                arr[j][k] =1
for i in range(n):
    print(*arr[i])
