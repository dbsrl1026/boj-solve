import sys

test = int(sys.stdin.readline())
for _ in range(test):
    dic = {}
    n = int(sys.stdin.readline())
    for i in range(n):
        v, k = map(str,sys.stdin.readline().split())
        if k not in dic:
            dic[k] = 1
        dic[k]+=1
    sum =1
    for v in dic.values():
        sum *= v
    print(sum-1)
