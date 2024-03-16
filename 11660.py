import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0]
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for i, v in enumerate(temp):
        arr.append(arr[-1] + v)

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sum = 0
    for i in range(x1, x2 + 1):
        sum += arr[(i - 1) * n + y2] - arr[(i - 1) * n + y1 - 1]
    print(sum)