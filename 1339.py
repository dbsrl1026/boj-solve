n = int(input())
words = [0] * 26
offset = ord('A')
for _ in range(n):
    temp = list(reversed(input()))
    for i in range(len(temp)):
        words[ord(temp[i]) - offset] += 10**i

words = sorted(words, reverse=True)
answer = 0
for i in range(10):
    answer += words[i] * (9-i)
print(answer)
