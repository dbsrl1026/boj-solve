import sys

n = int(sys.stdin.readline())
str1 = list(map(int, sys.stdin.readline().split()))
str2 = sorted(list(set(str1)))
m = len(str2)
arr = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            arr[i][j] = arr[i-1][j - 1]+ 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
print(arr[n][m])
