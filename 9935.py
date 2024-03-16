s = list(input())
bomb = list(input())
output = []


def searchBomb():
    global output
    k = len(output)
    l = len(bomb)
    for i in range(l):
        if k-1-i<0 or output[k-1-i] != bomb[l-1-i]:
            return
    for _ in range(l):
        output.pop()
    return

for i in range(len(s)):
    output.append(s[i])
    if output[-1] == bomb[-1]:
        searchBomb()
output = ''.join(map(str, output))
if output == '':
    print('FRULA')
else:
    print(output)
