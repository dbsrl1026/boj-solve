import math
n = int(input())
arr = list(map(int, input().split()))
t, p = map(int,input().split())

shirts = 0
for i in arr:
    shirts += math.ceil(i/t)
print(shirts)

pen = math.floor(n / p)
rest = n % p
print(pen, rest)