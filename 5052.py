def test(n):
    phones = {}
    switch = 0
    for _ in range(n):
        phones[input()] = True

    for k in phones.keys():
        for i in range(1,len(k)):
            if k[:i] in phones:
                switch = 1
    if switch == 0:
        print('YES')
    else:
        print('NO')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    test(n)