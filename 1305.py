l = int(input())
pattern = list(input())
lps = [0] * l
# lps 계산
i = 0
for j in range(1,l):

    while i > 0 and pattern[i] != pattern[j]:
        i = lps[i-1]

    if pattern[i] == pattern[j]:
        i += 1
        lps[j] = i

print(l - lps[l-1])

