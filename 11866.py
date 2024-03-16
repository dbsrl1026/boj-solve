n, k = map(int, input().split())
arr=[]
seq = []
for i in range(1,n + 1):
    arr.append(i)

count = 0
while arr:
    count += k-1
    count %= len(arr)
    seq.append(arr.pop(count))
print('<'+str(seq)[1:-1]+'>')