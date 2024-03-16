n, q = map(int, input().split())
arr = {}
revArr = {}
for i in range(n):
    temp = input()
    arr[i] = temp
    revArr[temp] = i
for i in range(q):
    temp = input()
    if str.isdigit(temp):
        temp = int(temp)
        print(arr[temp-1])
    else:
        print(int(revArr[temp])+1)
