testCase = int(input())
b1 = int(input())
arr1 = []
arr1 = list(map(int, input().split()))
b2 = int(input())
arr2 = []
arr2 = list(map(int, input().split()))
arr1 = sorted(arr1)
for _ in range(testCase):
    for i in range(b2):
        n = arr2[i]
        lo = 0
        hi = b1-1
        while(lo<=hi):
            mid = (lo + hi) // 2
            if arr1[mid] == n:
                print(1)
                break
            elif arr1[mid] < n:
                lo = mid +1
            else:
                hi = mid -1
            if lo > hi:
                print(0)

