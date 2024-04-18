test = int(input())
for _ in range(test):
    n = int(input())
    arr= list(map(int, input().split()))
    maxx = arr[n-1]
    answer = 0
    for  i in range(n-2, -1 , -1):
        if arr[i] < maxx:
            answer+= maxx - arr[i]
        else:
            maxx = arr[i]
    print(answer)