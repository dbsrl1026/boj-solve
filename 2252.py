import sys
input = sys.stdin.readline
from collections import defaultdict, deque
n,m = map(int, input().split())
degree = [0] * (n+1)
dict = defaultdict(list)
queue = deque()
answer = []

for i in range(m):
    a,b = map(int, input().split())
    dict[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    temp = queue.popleft()
    for next in dict[temp]:
        degree[next] -= 1
        if degree[next] == 0:
            queue.append(next)
    answer.append(temp)

print(*answer)