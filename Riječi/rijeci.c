# include <stdio.h>

// fibonacci sequence

int main() 
{
    int K; 
    scanf( "%d", &K );

    int fib[ K + 1 ];
    fib [ 0 ] = 0;
    fib [ 1 ] = 1;

    for ( int i = 2; i <= K; i++ ) {
        fib[ i ] = fib[ i - 2 ] + fib[ i - 1 ];
    }

    printf( "%d %d\n", fib[ K - 1 ], fib[ K ] );
}