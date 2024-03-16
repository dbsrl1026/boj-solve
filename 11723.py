import sys

n = int(sys.stdin.readline())
arr= []
for _ in range(n):
    inst = list(map(str, sys.stdin.readline().rstrip().split()))
    if inst[0] == 'add':
        if inst[1] not in arr:
            arr.append(inst[1])
    elif inst[0] == 'remove':
        if inst[1] in arr:
            arr.remove(inst[1])
    elif inst[0] == 'check':
        if inst[1] in arr:
            print(1)
        else:
            print(0)
    elif inst[0] == 'toggle':
        if inst[1] not in arr:
            arr.append(inst[1])
        else:
            arr.remove(inst[1])
    elif inst[0] == 'all':
        arr = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    elif inst[0] == 'empty':
        arr = []