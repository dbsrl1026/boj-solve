n = int(input())

minus = []
plus = []
zero = []
for _ in range(n):
    m = int(input())
    if m == 0:
        zero.append(m)
    elif m > 0:
        plus.append(m)
    else:
        minus.append(m)

plus.sort(reverse=True)
minus.sort()
count = 0
while True:
    if len(plus) > 1:
        if plus[0] + plus[1] > plus[0] * plus[1]:
            count += plus[0] + plus[1]
        else:
            count += plus[0] * plus[1]
        del plus[1], plus[0]
    if len(plus) == 1:
        count += plus[0]
        del plus[0]
    if len(minus) > 1:
        count += minus[0] * minus[1]
        del minus[1], minus[0]
    if len(minus) == 1 and len(zero) == 0:
        count += minus[0]
        del minus[0]
    if len(plus) == 0 and len(minus) <= 1:
        break

print(count)
