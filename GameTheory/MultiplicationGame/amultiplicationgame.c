#include <stdio.h>
#include <stdbool.h>

int main() {
    long long n;
    while ( scanf( "%lld", &n ) == 1 ) {
        long long current = 1;
        bool turn = true; // true for Stan, false for Ollie

        while (current < n) {
            current *= (turn) ? 9 : 2; // Stan multiplies by 9, Ollie by 2
            if ( current >= n ) break;
            turn = !turn; // Switch turn
        }

        if ( turn ) {
            printf("Stan wins.\n");
        } else {
            printf("Ollie wins.\n");
        }
    }
}
