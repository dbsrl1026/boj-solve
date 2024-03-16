import sys

n, l = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(arr)
while True:
    sum = 0
    mid = int((start + end) / 2)
    for i, v in enumerate(arr):
        if v > mid:
            sum += v - mid
    if sum == l or start == end -1:
        break
    elif sum <l:
        end = mid
    else :
        start = mid
print(mid)
