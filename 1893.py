import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    answer = []
    alphabets = {}
    index = list(input().rstrip())
    for i in range(len(index)):
        alphabets[index[i]] = i
    ori_text = list(input().rstrip())
    cipher_text = list(input().rstrip())

    len_index = len(index)
    len_ori_text = len(ori_text)
    len_cipher_text = len(cipher_text)
    lps = [0] * len_ori_text
    i = 0
    for j in range(1, len_ori_text):
        while i > 0 and ori_text[i] != ori_text[j]:
            i = lps[i-1]

        if ori_text[i] == ori_text[j]:
            i += 1
            lps[j] = i

    for i in range(len_index):
        shifted = []
        for j in range(len_ori_text):
            temp = alphabets[ori_text[j]]
            if temp + i >= len_index:
                shifted.append(index[temp + i - len_index])
            else:
                shifted.append(index[temp + i])
        cnt = 0
        j = 0
        for k in range(len_cipher_text):
            while j > 0 and cipher_text[k] != shifted[j]:
                j = lps[j-1]

            if cipher_text[k] == shifted[j]:
                j += 1
                if j == len_ori_text:
                    cnt += 1
                    j = lps[j-1]
        if cnt == 1:
            answer.append(i)

    if len(answer) == 0:
        print("no solution")
    elif len(answer) == 1:
        print("unique: " + str(answer[0]))
    else:
        print("ambiguous: " + ' '.join(map(str, answer)))


    