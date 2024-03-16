import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr, reverse=True)
sum = 0
for i, v in enumerate(arr):
    sum += v * (i + 1)
print(sum)
