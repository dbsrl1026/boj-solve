arr = []
next = 0
for i in range(3):
    arr.append(input().split()[0])
    if arr[i] != 'Fizz' and arr[i] != 'Buzz' and arr[i] != 'FizzBuzz':
        next = int(arr[i]) + 3 - i
if next % 3 == 0 and next % 5 == 0:
    print("FizzBuzz")
elif next % 3 == 0:
    print("Fizz")
elif next % 5 == 0:
    print("Buzz")
else:
    print(next)