n,m = map(int, input().split())
s = list(input())
answer = 0
dict = {}
dict['A'], dict['C'], dict['G'], dict['T'] = map(int, input().split())
for i in range(m):
    dict[s[i]] -= 1
if all(x <= 0 for x in dict.values()):
    answer += 1
for i in range(m, n):
    dict[s[i]] -= 1
    dict[s[i - m]] += 1
    if all(x <= 0 for x in dict.values()):
        answer += 1
print(answer)
