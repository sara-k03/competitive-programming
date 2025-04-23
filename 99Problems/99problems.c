#include <stdio.h>

int main() {
    int n;
    scanf( "%d", &n );

    int result;

    if ( n <= 99 ) {
        result = 99;
    } else {

        int lower = ( n / 100 ) * 100 - 1;
        int higher = ( n / 100 ) * 100 + 99;

        if ( n - lower < higher - n ) {
            result = lower;
        } else {
            result = higher;
        }

    }

    printf( "%d", result );
}