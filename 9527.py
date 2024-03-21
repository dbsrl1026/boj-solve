import sys
import math
sys.setrecursionlimit(10**8)
a, b = map(int, input().split())


def dnc(x):
    if x <= 0:
        return 0
    jyo = int(math.log2(x))
    floor_2pow = 2 ** jyo 
    if floor_2pow == x:
        return jyo * x // 2 + 1

    diff = x - floor_2pow
    return dnc(floor_2pow) + diff + dnc(diff)


print(dnc(b) - dnc(a-1))