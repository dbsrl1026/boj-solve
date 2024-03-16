n = int(input())
arr = []
result = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for i,v in enumerate(arr):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if v[0]<arr[j][0] and v[1]< arr[j][1]:
            count+=1
    result.append(count+1)

print(*result)
