from collections import defaultdict, deque

n = int(input())
arr = list(map(int, input().split()))

cur_var = 0
queue = deque()
dict = defaultdict(int)
max_length = 0


for v in arr:
    queue.append(v)
    if dict[v] == 0:
        cur_var += 1
        while cur_var > 2:
            temp = queue.popleft()
            dict[temp] -= 1
            if dict[temp] == 0:
                cur_var -= 1
    dict[v] += 1
    max_length = max(max_length, len(queue))
print(max_length)

