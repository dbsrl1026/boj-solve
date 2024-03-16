import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp <= k:
        arr.append(temp)
arr = sorted(arr)
cnt = 0
while k > 0 :
    tmp = arr.pop()
    charge = int(k/tmp)
    k -= charge* tmp
    cnt += charge
print(cnt)