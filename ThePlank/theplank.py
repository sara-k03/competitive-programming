n = int(input())

if n == 0:
    print(1)
elif n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    arr = [0] * (n + 1)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

    print( arr[n] )