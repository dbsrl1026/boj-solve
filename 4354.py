while 1:
    string = list(input())
    if string[0] == '.':
        exit(0)

    length = len(string)
    square = [0] * length
    lps = [0] * length
    i = 0
    for j in range(1, length):
        while i > 0 and string[i] != string[j]:
            i = lps[i-1]
        if string[i] == string[j]:
            i+= 1
            lps[j] = i
    base = length - 1
    while base > 0 and lps[base-1] != 0 and lps[base-1] < lps[base]:
        base -= 1

    if base == 0:
        base += 1


    if lps[length-1] % base != 0:
        print(1)
    else:
        print(lps[length-1] // base + 1)

