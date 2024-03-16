import sys

def r_(n): return int(n)+1 if n-int(n)>=0.5 else int(n)

n = int(sys.stdin.readline())
if n == 0 :
    print(0)
    exit()
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)
sum = 0
cut = int(r_(n * 0.15))
for i in range(cut, n - cut):
    sum += arr[i]
average = int(r_(sum / (n - cut * 2)))
print(average)
