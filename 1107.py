import sys

chan = int(sys.stdin.readline())
num = int(sys.stdin.readline())
dic = {}
arr= list(map(str,sys.stdin.readline().split()))
for _,v in enumerate(arr):
    dic[v] = True

def judge(digit,dic):
    for _, v in enumerate(digit):
        if v in dic:
            return False
    return True
minMove = 500000
for i in range(1000000):
    digit = list(str(i))
    if not judge(digit,dic):
        continue
    move = len(digit) + abs(chan-i)
    if move < minMove:
        minMove = move

print(min(minMove,abs(chan - 100)))
