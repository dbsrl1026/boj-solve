N, F = map(int, input().split())

Fact = [0] * N
Mul = [0] * N
check = [0] * (N + 1)
answer = [0] * N

Fact[0] = 1
for i in range(1, N):
    Fact[i] = Fact[i - 1] * i

for i in range(N):
    Mul[i] = Fact[N - 1] // (Fact[N - 1 - i] * Fact[i])

def DFS(K, ans):
    global flag
    if flag or ans > F:
        return

    if K == N:
        if F == ans:
            print(*answer)
            flag = 1
        return
    for i in range(1, N + 1):
        if not check[i]:
            check[i] = 1
            answer[K] = i
            DFS(K + 1, ans + (Mul[K] * i))
            if flag:
                break
            check[i] = 0
flag = 0
DFS(0, 0)