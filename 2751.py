n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr)
for i,v in enumerate(arr):
    print(v)