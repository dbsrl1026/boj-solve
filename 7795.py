test= int(input())
for _ in range(test):
    lenA, lenB = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    cnt = 0
    j = 0
    for i in range(lenA):
        while j < lenB and a[i] > b[j]:
            j += 1
        cnt += j
    print(cnt)

