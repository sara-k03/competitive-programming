def power(a, e, m):
    result = 1
    while e:
        if e & 1:
            result = (result * a) % m
        a = (a * a) % m
        e >>= 1
    return result

line = input()
line = line.split()
a = int(line[0])
e = int(line[1])
m = int(line[2])

print( power( a, e, m ) )