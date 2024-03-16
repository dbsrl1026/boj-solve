n = int(input())
col = [True]*n
dia1 = [True]*(2*n-1)
dia2 = [True]*(2*n-1)
cnt = 0
def nQueens(i):
    global cnt
    for j in range(n):
        if col[j] == True and dia1[j-i+n-1]==True and dia2[j+i]==True:
            if i == n-1:
                cnt+=1
            else:
                col[j] = False; dia1[j - i + n-1] = False; dia2[j + i] = False
                nQueens(i+1)
                col[j] = True; dia1[j - i + n-1] = True;  dia2[j + i] = True
nQueens(0)
print(cnt)