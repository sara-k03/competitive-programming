n = int( input() )
ids = list( int(input()) for _ in range(n) )

while True:
    unique = set()
    for i in ids:
        unique.add( i % n ) # starts at the number of IDs
    if ( len( unique ) == len( ids ) ): # if the number of unique IDs is equal to the number of ids, they're all unique
        print( n )
        break
    n = n + 1