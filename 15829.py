import sys

l = int(sys.stdin.readline())
str = list(sys.stdin.readline())
sum = 0
for i in range(l):
    temp = ord(str[i]) -96
    sum += temp*(31**i)
answer = sum % 1234567891
print(answer)
