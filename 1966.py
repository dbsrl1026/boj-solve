from collections import deque

testCase = int(input())
ans =[]
for _ in range(testCase):
    num, doc = map(int,input().split())
    arr= deque()
    arr.extend(map(int,input().split()))
    count = 0
    while True:
        if arr[0] == max(arr):
            arr.popleft()
            count+=1
            if doc == 0:
                break
            else:
                doc -= 1
        else:
            arr.append(arr.popleft())
            if doc == 0:
                doc += len(arr)
            doc -=1
    ans.append(count)
for _,v in enumerate(ans):
    print(v)


