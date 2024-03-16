import sys
from collections import deque

test = int(sys.stdin.readline())
for _ in range(test):
    error = False
    reverse = 1
    func = deque(sys.stdin.readline().rstrip())
    num = int(sys.stdin.readline())
    if num == 0:
        arr = sys.stdin.readline()
        arr = []
    else:
        arr = deque(map(int,sys.stdin.readline().rstrip().replace('[','').replace(']','').split(',')))

    while func:
        v = func.popleft()
        if v == 'R':
            reverse *=-1
        elif v == 'D':
            if arr:
                if reverse == 1:
                   arr.popleft()
                else:
                    arr.pop()
            else:
                error = True
                break
    if error:
        print('error')
    else:
        arr = list(arr)
        if reverse == -1:
            arr = list(reversed(arr))
        print(str(arr).replace(' ', ''))

