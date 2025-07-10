from fractions import Fraction

n = int(input())
pattern = list(input().split())
all = list(input().split())
for i in range(len(all)-1):
    all.append(all[i])
length = len(pattern)
lps = [0] * length

# lps 계산
i = 0
for j in range(1,length):

    while i > 0 and pattern[i] != pattern[j]:
        i = lps[i-1]

    if pattern[i] == pattern[j]:
        i += 1
        lps[j] = i

cnt = 0
i = 0

# kmp
for j in range(len(all)):

    while i > 0 and pattern[i] != all[j]:
        i = lps[i-1]

    if all[j] == pattern[i]:
        i += 1
        if i == length:
            cnt += 1
            i = lps[i-1]



answer = Fraction(cnt, n)
if answer == 1:
    print("1/1")
else:
    print(answer)
