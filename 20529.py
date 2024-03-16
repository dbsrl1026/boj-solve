import sys

t = int(sys.stdin.readline())


def calculateDistance(n1, n2):
    cnt = 0
    for i in range(4):
        temp1 = n1 // 10 ** (3 - i)
        temp2 = n2 // 10 ** (3 - i)
        if temp1 != temp2:
            cnt += 1
        n1 -= temp1 * 10 ** (3 - i)
        n2 -= temp2 * 10 ** (3 - i)
    return cnt


for _ in range(t):
    dic = {}
    n = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().rstrip().split())
    for i, v in enumerate(arr):
        temp = 0
        if v[:1] == 'E':
            temp += 1000
        if v[1:2] == 'S':
            temp += 100
        if v[2:3] == 'T':
            temp += 10
        if v[3:4] == 'P':
            temp += 1
        if temp not in dic:
            dic[temp] = 1
        else:
            dic[temp] += 1
    minn = 8
    for k, v in dic.items():
        if v >= 3:
            minn = 0
            break
        elif v == 2:
            for k2, v2 in dic.items():
                if v2 > 0 and k != k2:
                    minn = min(minn, 2 * calculateDistance(k, k2))
        elif v == 1:
            for k2, v2 in dic.items():
                if v2 > 0 and k != k2:
                    for k3, v3 in dic.items():
                        if v3 > 0 and k != k2 and k2 != k3 and k != k3:
                            minn = min(minn, calculateDistance(k, k2) + calculateDistance(k,
                                                                                          k3) + calculateDistance(
                                k2, k3))
    print(minn)
