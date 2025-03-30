#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    // Euclid's formula: https://en.wikipedia.org/wiki/Pythagorean_triple  
    for (int m = 2; m * m < n; m++) {
        for (int n_val = 1; n_val < m; n_val++) {
            if ((m - n_val) % 2 == 1) {  
                int a = m * m - n_val * n_val;
                int b = 2 * m * n_val;
                int c = m * m + n_val * n_val;
                int sum = a + b + c;

                // scaling
                if (n % sum == 0) {
                    int k = n / sum;
                    printf("%d %d %d\n", k * a, k * b, k * c);
                    return 0;
                }
            }
        }
    }

    printf("0 0 0\n"); 
    return 0;
}
