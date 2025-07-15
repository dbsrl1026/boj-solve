n = int(input())
rest = n % 5

if rest == 1 or rest == 3 or rest == 4:
    print("SK")
else:
    print("CY")