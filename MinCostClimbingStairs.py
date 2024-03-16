def mccs(input):
    table={0:input[0], 1:input[1]}
    for i in range(2,len(input)):
        table[i] = min(table[i-1],table[i-2]) + input[i]
    return min(table[len(input)-1],table[len(input)-2])




input = [10,15,20]
print(mccs(input))