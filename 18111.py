n,m,b = map(int,input().split())
arr = []
for i in range(n):
    arr.extend(list(map(int,input().split())))

arr = sorted(arr)
if n*m%3 == 0:
    median = arr[int(n*m*2/3+1)]
else:
    median = arr[int(round(n*m*2/3))]

while True:
    bCopy = b
    time = 0
    for i ,v in enumerate(arr):
        if median - v >= 0:
            bCopy -= median - v
            time += median -v
        else:
            bCopy += v - median
            time += 2*(v - median)
    if bCopy<0:
        median-=1
    else:
        break
print(time, median)