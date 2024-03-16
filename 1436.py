N = int(input())
cnt = 665
while N>0:
    cnt+=1
    arr = list(str(cnt))
    for i in range(len(arr)-2):
        if arr[i] == '6' and arr[i+1] == '6' and arr[i+2] == '6':
            N-=1
            temp = cnt
            break

print(cnt)