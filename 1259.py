arr =[]
while True:
    tmp = input()
    if tmp == '0':
        break
    tmp = list(tmp)
    for i in range(len(tmp)):
        if tmp[i] != tmp[len(tmp)-i-1]:
            print('no')
            break
        elif i == len(tmp)-1:
            print('yes')

