#include <stdio.h>

int main() {
    unsigned long long a;
    unsigned long long b;
    unsigned long long c;

    scanf( "%llu %llu %llu", &a, &b, &c );

    if ( a + b == c ) {
        printf( "%lld+%lld=%lld\n", a, b, c );
    } else if ( a - b == c ) {
        printf( "%lld-%lld=%lld\n", a, b, c );
    } else if ( a * b == c ) {
        printf( "%lld*%lld=%lld\n", a, b, c );
    } else if ( b != 0 && a / b == c ) {
        printf( "%lld/%lld=%lld\n", a, b, c );
    } else if ( a == b + c ) {
        printf( "%lld=%lld+%lld\n", a, b, c );
    } else if ( a == b - c ) {
        printf( "%lld=%lld-%lld\n", a, b, c );
    } else if ( a == b * c ) {
        printf( "%lld=%lld*%lld\n", a, b, c );
    } else if ( c != 0 && a == b / c ) {
        printf( "%lld=%lld/%lld\n", a, b, c );
    }
}