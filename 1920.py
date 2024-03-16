N = int(input())
dic ={}
arr=list(map(int, input().split()))
for i in range(N):
    dic[arr[i]] = 1
M = int(input())
arr2 = list(map(int, input().split()))
for i in range(M):
    if arr2[i] in dic:
        print(1)
    else:
        print(0)