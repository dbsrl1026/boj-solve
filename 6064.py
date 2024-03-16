import sys
import math


def lcm(a, b):
    return a * b / math.gcd(a, b)


test = int(sys.stdin.readline())
for _ in range(test):
    m, n, x, y = map(int, sys.stdin.readline().split())
    for i in range(int(lcm(n, m) / m)):
        k = (m * i + x - y) / n
        if k == int(k):
            print(x + i * m)
            break
        elif i == int(lcm(n, m) / m)-1:
            print(-1)

