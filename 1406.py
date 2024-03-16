from collections import deque

string = input().rstrip()
left_stack = deque(string)
right_stack = deque()

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'L':
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

print(''.join(left_stack) + ''.join(right_stack))