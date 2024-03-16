import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr = sorted(arr, key=lambda x:(x[1],x[0]))
for i, v  in enumerate(arr):
    print(v[0],v[1])