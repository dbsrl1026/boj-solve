def combination(a, b):
    c = 1
    for i in range(b):
        c *= a - i
        c /= b - i
    return c


p1 = int(input()) / 100
p2 = int(input()) / 100
prime = [2, 3, 5, 7, 11, 13, 17]

t1 = 0
t2 = 0
for v in prime:
    t1 += p1 ** v * (1 - p1) ** (18 - v) * combination(18, v)
    t2 += p2 ** v * (1 - p2) ** (18 - v) * combination(18, v)

answer = t1 + t2 - t1 * t2
print(answer)
