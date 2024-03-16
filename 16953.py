from collections import deque

a, b = map(int, input().split())

queue = deque()

queue.append((a, 1))

while queue:
    node, cnt = queue.popleft()
    if node == b:
        print(cnt)
        exit(0)
    if node * 2 <= b:
        queue.append((node * 2, cnt + 1))
    if node * 10 + 1 <= b:
        queue.append((node * 10 + 1, cnt + 1))

print(-1)