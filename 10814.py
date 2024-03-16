n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str,input().split())))
    arr[i][0] = int(arr[i][0])

arr = sorted(arr,key= lambda x : x[0])
for i ,v in enumerate(arr):
    print(v[0],v[1])