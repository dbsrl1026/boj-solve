def findSosu(k):
    if k ==1 :
        return 0
    for i in range(2,int(k**0.5+1)):
        if k%i == 0:
            return 0
    return 1

n = int(input())
arr=list(map(int,input().split()))
count = 0
for i in range(n):
    if findSosu(arr[i]) == 1:
        count+=1
print(count)
