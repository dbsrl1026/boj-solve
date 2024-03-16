from collections import deque

n = int(input())
bridges = list(map(int, input().split()))
start, end = map(int, input().split())

queue = deque()
queue.append((start, 0))
while queue:
    node, cnt = queue.popleft()
    if node == end:
        print(cnt)
        exit(0)
    tempToPlus = node
    tempToMinus = node
    while tempToPlus + bridges[node - 1] < n:
        tempToPlus += bridges[node - 1]
        queue.append((tempToPlus, cnt + 1))
    while tempToMinus - bridges[node - 1] > 1:
        tempToMinus -= bridges[node - 1]
        queue.append((tempToMinus, cnt + 1))
print(-1)
