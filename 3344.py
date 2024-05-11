N = int(input())
col = 2
if N % 6 == 2:
    cnt = N - 4
    while cnt > 0:
        print(col)
        col += 2
        if col > N:
            print(3)
            print(1)
            col = 7
        cnt -= 1
    print(col)
    print(5)
elif N % 6 == 3:
    col = 4
    cnt = N - 3
    while cnt > 0:
        print(col)
        col += 2
        if col > N and col % 2 == 0:
            print(2)
            col = 5
        cnt -= 1
    print(1)
    print(3)
else:
    for i in range(1, N+1):
        print(col)
        col += 2
        if col > N:
            col = 1