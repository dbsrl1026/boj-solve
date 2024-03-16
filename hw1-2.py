n = int(input())
arr1=[]
arr2=[]

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1Sorted = sorted(arr1)
arr2Sorted = sorted(arr2, reverse=True)
sum = 0
for i in range(n):
    sum += arr1Sorted[i] * arr2Sorted[i]
print(sum)
