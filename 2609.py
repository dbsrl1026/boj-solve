from collections import deque


def soinsu(num):
    arr = []
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            arr.append(i)
            arr.extend(soinsu(int(num/i)))
            return arr
    arr.append(num)
    return arr

m,n = map(int,input().split())
if m == 1 or n == 1:
    print(1)
    print(m*n)
    exit()
num1 = deque()
num2 = deque()
num1.extend(soinsu(m))
num2.extend(soinsu(n))
stack = []
gys = []
while True:
    if len(num1) == 0 and len(num2) == 0:
        break
    elif len(num2) == 0:
        stack.append(num1.popleft())
    elif len(num1) == 0:
        stack.append(num2.popleft())
    elif num1[0] < num2[0]:
        stack.append(num1.popleft())

    elif num1[0] > num2[0]:
        stack.append(num2.popleft())
    elif num1[0] == num2[0]:
        num1.popleft()
        gys.append(num2.popleft())
ans = 1
for i,v in enumerate(gys):
    ans *= v
print(ans)
for i,v in enumerate(stack):
    ans *= v
print(ans)