import math

n = int(input())
input()

for i in range(n):
    sum = 0
    num_kids = int(input())
    for j in range(num_kids):
        sum += int(input())
    
    if sum % num_kids == 0:
        print("YES")
    else:
        print("NO")

    if i != n - 1:
        input()