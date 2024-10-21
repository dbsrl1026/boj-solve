import math

n, p, q = map(int, input().split())

dict = {0 : 1}
def topdown(k):
    if k not in dict:
        dict[k] = topdown(math.floor(k / p)) + topdown(math.floor(k / q))
    return dict[k]
print(topdown(n))
