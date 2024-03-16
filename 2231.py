n = int(input())
sangsung = []
for i in range(1,n):
    k = i
    arr = []
    while k>=1:
        arr.append(k%10)
        k = int(k/10)
    if i+sum(arr) == n:
        sangsung.append(i)
if len(sangsung) == 0:
    print(0)
else:
    print(min(sangsung))
