S = str(input())
S_list = list(S)

N = int(input())
dp = [0] * (len(S_list) + 1)
dp[0] = 1

words = []
for _ in range(N):
    word = str(input().rstrip())
    words.append(word)

for i in range(len(S_list) + 1):
    for word in words:
        word_len = len(word)
        if i >= word_len and dp[i - word_len] == 1 and S_list[i - word_len:i] == list(word):
            dp[i] = 1

if dp[len(S_list)]:
    print(1)
else:
    print(0)