n, m = map(int,input().split())
hear = {}
see = {}
for i in range(n):
    hear[input()] = True
for i in range(m):
    see[input()] = True

common = []
for k in hear.keys():
    if k in see:
        common.append(k)
common = sorted(common)
print(len(common))
for i,v in enumerate(common):
    print(v)