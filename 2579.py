import sys

memo = {}
rmemo = {}
def dfs(arr,n,pPop):
    if n==1:
        return memo[1]
    elif n==2:
        if pPop == n+1:
            return arr[n]
        else:
            return arr[n] + rmemo[1]
    else:
        if pPop == n+1:
            if n-2 not in memo:
                memo[n-2] = dfs(arr,n-2,n)
            return arr[n]+ memo[n-2]
        else:
            if n-1 not in rmemo:
                rmemo[n-1] = dfs(arr,n-1,n)
            if n-2 not in memo:
                memo[n-2] = dfs(arr,n-2,n)
            return arr[n] + max(rmemo[n-1],memo[n-2])

n = int(sys.stdin.readline())
arr= [0]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
if n ==1:
    print(arr[1])
    exit()
elif n ==2:
    print(arr[1]+arr[2])
    exit()
memo[1] = arr[1]
memo[2] = arr[1]+arr[2]
rmemo[1] = arr[1]
rmemo[2] =arr[2]
print(dfs(arr,n,10002))