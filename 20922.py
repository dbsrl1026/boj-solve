from collections import defaultdict

n, k = map(int,input().split())
arr = list(map(int,input().split()))
dict = defaultdict(int)
maxx = 0
cnt = 0
p2 = 0
for i in range(n):
    cnt += 1
    dict[arr[i]] += 1
    while dict[arr[i]] > k:
        dict[arr[p2]] -= 1
        cnt -= 1
        p2 += 1
    maxx = max(maxx, cnt)
print(maxx)