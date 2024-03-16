n = int(input())
k5 = int(n/5)
k3=0
while k5>=0:
    if (n - k5*5)%3 == 0:
        k3 = int((n - k5*5)/3)
        break
    else:
        k5-=1
if k5<0:
    print(-1)
else:
    print(k5+k3)