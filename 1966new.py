from collections import deque

test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    prior = deque(map(int, input().split()))
    cnt = 0
    while 1:
        maxx = max(prior)
        tmp = prior.popleft()
        if m == 0 and tmp == maxx:
            cnt += 1
            break
        m -= 1
        m %= n
        if tmp != maxx:
            prior.append(tmp)
        else:
            cnt += 1
            n -= 1
    print(cnt)
