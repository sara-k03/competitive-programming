#include <stdio.h>

int main() {
    unsigned long long one;
    unsigned long long two;
    while ( scanf( "%llu %llu", &one, &two ) == 2 ) {
        long long diff;
        if ( one > two ) {
            diff = one - two;
        } else {
            diff = two - one;
        }

        printf( "%lld\n", diff );
    }
}