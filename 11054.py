n = int(input())
arr = list(map(int, input().split()))
bu = []
td = []

for i in range(n):
    if i == 0:
        bu.append(1)
        continue
    maxx = 0
    for j in range(i):
        if arr[j]<arr[i]:
            maxx = max(maxx, bu[j])
    bu.append(maxx+1)

for i in range(n-1,-1,-1):
    if i == n-1:
        td.append(1)
        continue
    maxx = 0
    for j in range(n-1,i,-1):
        if arr[j] <arr[i]:
            maxx = max(maxx, td[n-1-j])
    td.append(maxx+1)
for i in range(n):
    bu[i]+= td[n-1-i]
print(max(bu)-1)