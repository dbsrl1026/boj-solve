def zegop(mat1,mat2):
    n = len(mat1[0])
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += mat1[i][k] * mat2[k][j]
            temp[i][j] = temp[i][j]%1000
    return temp

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))





bit = []
bit.append(matrix)
while 2 ** (len(bit)) - 1 < m:
   bit.append(zegop(bit[-1],bit[-1]))

result = [[0] * n for _ in range(n)]
for i in range(n):
    result[i][i] = 1


for i in range(len(bit)-1,-1,-1):
    if 2**i <=m:
        result = zegop(result,bit[i])
        m -= 2**i
for i in range(n):
    print(*result[i])