import sys

n = int(sys.stdin.readline())
m = list(map(str, sys.stdin.readline().strip()))
answer = []
blue = 0
red = 0
cnt = 0

for i in range(n):
    if m[i] == "R":
        red += 1
    if m[i] == "B" and red:
        cnt += red
        red = 0
answer.append(cnt)


cnt = 0
for i in range(n):
    if m[i] == "B":
        blue += 1
    if m[i] == "R" and blue:
        cnt += blue
        blue = 0
answer.append(cnt)

m.reverse()
cnt = 0
red = 0
for i in range(n):
    if m[i] == "R":
        red += 1
    if m[i] == "B" and red:
        cnt += red
        red = 0
answer.append(cnt)

blue = 0
cnt = 0
for i in range(n):
    if m[i] == "B":
        blue += 1
    if m[i] == "R" and blue:
        cnt += blue
        blue = 0
answer.append(cnt)
print(min(answer))
