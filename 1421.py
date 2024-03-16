n, c, w = map(int, input().split())

namu=[]

for i in range(n):
    namu.append(int(input()))

maxx=0

for i in range(1,max(namu)+1):
    temp=0
    for j in range(n):
        count, remain = divmod(namu[j],i)

        if remain:
            expense = count * c

        else :
            expense =(count-1) *c

        target =  (count * w * i) - expense

        if target < 0:
            continue

        temp += target

        if temp > maxx:
            maxx=temp


print(maxx)
