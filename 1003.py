

arr=[]

inp=[]
num = int(input())

for i in range(41):
    arr.append([])
    if i==0:
        arr[i].append(1)
        arr[i].append(0)
    elif i==1:
        arr[i].append(0)
        arr[i].append(1)
    else:
        arr[i].append(arr[i-1][0]+arr[i-2][0])
        arr[i].append(arr[i - 1][1] + arr[i - 2][1])



for i in range(num):
    inp.append(int(input()))

for i in range(num):
    print(arr[inp[i]][0], arr[inp[i]][1])