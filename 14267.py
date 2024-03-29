import sys
input = sys.stdin.readline

n, m = map(int, input().split())
workers = list(map(int, input().split()))
praises = [0] * (n + 1)

for _ in range(m):
    object, degree = map(int, input().split())
    praises[object] += degree

for i in range(2, n + 1):
    praises[i] += praises[workers[i-1]]

praises.pop(0)
print(*praises)
