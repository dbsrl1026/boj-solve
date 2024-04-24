a, b = map(int, input().split())
def zeroToX(x):
    sum = 0
    i = 1
    while i <= x:
        sum += i * ((x - i) // (i * 2) + 1)
        i *= 2
    return sum

print(zeroToX(b) - zeroToX(a-1))
