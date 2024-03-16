from collections import deque
from sys import stdin
n = int(stdin.readline())
queue = deque()

for i in range(n):
    command = list(map(str,stdin.readline().split()))
    if command[0] == 'push_front':
        queue.appendleft(int(command[1]))
    if command[0] == 'push_back':
        queue.append(int(command[1]))
    elif command[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])