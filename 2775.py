testCase = int(input())
for i in range(testCase):
    k= int(input())
    n= int(input())
    arr = [[0] * n for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                arr[i][j]=j+1
            else:
                for l in range(j+1):
                    arr[i][j] += arr[i-1][l]
    print(arr[k][n-1])