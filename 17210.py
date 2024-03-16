import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n):
   a,b = sys.stdin.readline().rstrip().split()
   dic[a] = b
for i in range(m):
    str = sys.stdin.readline().rstrip()
    print(dic[str])