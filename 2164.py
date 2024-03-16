from collections import deque

n = int(input())
arr=deque()

for i in range(n):
    arr.append(i+1)
count = 0
while arr:
    if n==1:
        temp = 1
        break
    temp = arr.popleft()
    if count % 2 == 1:
        arr.append(temp)
    count+=1
print(temp)