import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    arr = []
    arr.append(list(map(int, sys.stdin.readline().split())))
    arr.append(list(map(int, sys.stdin.readline().split())))
    run1 = {}
    run2 = {}
    for i in range(0,n):
        if i == 0:
            run1[i] = arr[0][0]
            run2[i] = arr[1][0]
        elif i == 1:
            run1[i] = arr[0][1]+run2[0]
            run2[i] = arr[1][1]+run1[0]
        else:
            run1[i] = max(run2[i-1],run2[i-2])+arr[0][i]
            run2[i] = max(run1[i-1],run1[i-2])+arr[1][i]
    print(max(run1[n-1],run2[n-1]))