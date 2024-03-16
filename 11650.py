import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr = sorted(arr, key=lambda x:(x[0],x[1]))
for i, v  in enumerate(arr):
    print(v[0],v[1])