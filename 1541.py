arr = list(input().split('-'))
for i in range(len(arr)):
    temp= list(map(int,arr[i].split('+')))
    arr[i] = 0
    for _,x in enumerate(temp):
        arr[i] += x
a =0
for i,v in enumerate(arr):
    if i == 0 :
        a= v
    else:
        a -= v
print(a)