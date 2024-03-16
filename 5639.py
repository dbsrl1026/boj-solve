import sys

root = int(sys.stdin.readline())
tree = [10 ** 6, root]

while True:
    try:
        temp = int(sys.stdin.readline())
        if temp < tree[-1]:
            tree.append(temp)
        else:
            for i in range(len(tree)-1,-1,-1):
                if temp < tree[i]:
                    for j in range(i + 2, len(tree)):
                        if tree[j] < tree[j - 1]:
                            for k in range(len(tree) - j):
                                print(tree.pop())
                            break
                    break
            tree.append(temp)
    except:
        break
for i in range(len(tree) - 1):
    print(tree.pop())
