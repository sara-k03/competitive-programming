from math import log2

def int_root(n, a): # function for taking a-th roots 
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        power = mid ** a
        if power == n:
            return mid
        elif power < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def pth_power(n):
    if n == 1:
        return 1
    if n == -1:
        return 1
    is_negative = n < 0
    abs_n = abs(n)
    max_a = int(log2(abs_n)) + 1
    if is_negative:
        if max_a % 2 != 0:
            start_a = max_a
        else: 
            start_a = max_a - 1
        for a in range(start_a, 1, -2):
            x = int_root(abs_n, a)
            if x != -1 and ((-x) ** a == n):
                return a
    else:
        for a in range(max_a, 1, -1):
            x = int_root(abs_n, a)
            if x != -1:
                return a
    return 1 

n = int(input())
while n != 0:
    print(pth_power(n))
    n = int(input())