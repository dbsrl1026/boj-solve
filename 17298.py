from collections import deque
n = int(input())
arr = deque(map(int,input().split()))

nge = deque()
nge.append([0,arr.popleft()])
ans = []

for i in range(1, len(arr)+1):
    temp = arr.popleft()
    while nge:
        if nge[-1][1] >= temp:
            break
        index, num = nge.pop()
        ans.append([index,temp])
    nge.append([i,temp])
while nge:
    index, num = nge.pop()
    ans.append([index, -1])

ans = sorted(ans)
for i in range(len(ans)):
    ans[i] = ans[i][1]
print(*ans)