mod = 10**9 + 7

def power(a, e, m):
    result = 1
    while e:
        if e & 1:
            result = (result * a) % m
        a = (a * a) % m
        e >>= 1
    return result

n = int(input())
for i in range( n ):
    value = int(input())
    print( ( 8 * power( 9, value - 1, mod ) ) % mod )
