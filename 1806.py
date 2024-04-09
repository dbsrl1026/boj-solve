from collections import deque

n, s = map(int, input().split())
arr = list(map(int, input().split()))
subArr = deque()
summ = 0
minn = n + 1
for e in arr:
    subArr.append(e)
    summ += e
    while summ >= s:
        minn = min(len(subArr),minn)
        summ -= subArr.popleft()

if minn == n+1:
    print(0)
else:
    print(minn)

