import sys
from collections import deque

n = int(sys.stdin.readline())


def left(d1,d2,d3,d4):
    return 1000 * d2 + 100 * d3 + 10 * d4 + d1


def right(d1,d2,d3,d4):
    return 1000 * d4 + 100 * d1 + 10 * d2 + d3


def double(num):
    return (num * 2) % 10000


def sub(num):
    if num == 0:
        return 9999
    else:
        return num - 1

def strSum(str1,str2):
    new_str = []
    new_str.append(str1)
    new_str.append(str2)
    return ''.join(new_str)


for _ in range(n):
    start, goal = map(int, sys.stdin.readline().split())
    visited = {}
    queue = deque()
    queue.append((start, ''))
    visited[start] =True
    while queue:
        (temp, inst) = queue.popleft()
        if temp == goal:
            break
        D = double(temp)
        if D not in visited:
            queue.append((D, strSum(inst,'D')))
            visited[D] = True
        S = sub(temp)
        if S not in visited:
            queue.append((S, strSum(inst,'S')))
            visited[S] = True
        d1 = int(temp / 1000)
        d2 = int((temp % 1000) / 100)
        d3 = int((temp % 100) / 10)
        d4 = temp % 10

        L = left(d1,d2,d3,d4)
        if L not in visited:
            queue.append((L, strSum(inst,'L')))
            visited[L] = True
        R = right(d1,d2,d3,d4)
        if R not in visited:
            queue.append((R, strSum(inst,'R')))
            visited[R] = True
    sys.stdout.write(inst+'\n')
