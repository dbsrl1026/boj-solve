from collections import defaultdict

n = int(input())
dict = defaultdict(bool)
arr = []
for i in range(2, n+1):
    if dict[i] == False:
        arr.append(i)
        j = 2
        while i * j <= n:
            dict[i*j] = True
            j += 1
p2 = 0
sum = 0
cnt = 0
for p1 in range(len(arr)):
    sum += arr[p1]
    while sum > n:
        sum -= arr[p2]
        p2 += 1
    if sum == n:
       cnt += 1

print(cnt)