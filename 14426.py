import sys

input = sys.stdin.readline

n, m = map(int, input().split())
S = []
for _ in range(n):
    S.append(input().strip())
S.sort()
answer = 0
s = []
for i in range(m):
    test = input().strip()
    s.append(test)
s.sort()
i = 0
j = 0
while i < n and j < m:
    if S[i][:len(s[j])] == s[j]:
        answer += 1
        j += 1
        continue
    elif S[i] > s[j]:
        j += 1
        continue
    elif S[i] < s[j]:
        i += 1
        continue
print(answer)
