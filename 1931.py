n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
start = 0
cnt = 0
arr = sorted(arr, key=lambda x:(x[1],x[0]))
for i,v in enumerate(arr):
    if v[0] >= start:
        cnt +=1
        start = v[1]
print(cnt)