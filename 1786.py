all = list(input())
pattern = list(input())
length = len(pattern)
lps = [0] * length

i = 0
for j in range(1, length):

    while i > 0 and pattern[i] != pattern[j]:
        i = lps[i-1]

    if pattern[i] == pattern[j]:
        i += 1
        lps[j] = i

i = 0
cnt = 0
index = []
for j in range(len(all)):
    while i > 0 and all[j] != pattern[i]:
        i = lps[i-1]

    if all[j] == pattern[i]:
        i += 1
        if i == length:
            cnt += 1
            index.append(str(j - i + 2))
            i = lps[i-1]

print(cnt)
print(' '.join(index))