import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().split()))
arrSum = sum(arr)
for _ in range(m):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    if e-s+1< m/2:
        ans = sum(arr[s-1:e])
    else:
        ans = arrSum - sum(arr[:s-1]) - sum(arr[e:])
    print(ans)