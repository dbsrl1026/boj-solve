
n = int(input())
m = int(input())
s = input()

ioi = 0
cnt = 0
i = 0
while i < m-2:
    if s[i:i+3] == 'IOI':
        ioi+=1
        if ioi == n:
            cnt +=1
            ioi -=1
        i+=2
    else:
        ioi = 0
        i+=1
print(cnt)