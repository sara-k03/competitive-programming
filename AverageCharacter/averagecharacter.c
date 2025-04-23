#include <stdio.h>

int main() 
{
    int sum = 0;
    int n = 0;
    int ch = getchar();
    while ( ch != '\n' && ch != EOF  ) {
        n++;
        sum += ch;
        ch = getchar();
    }
    double average = ( (double) sum ) / n;
    char average_int = (char) average;

    printf( "%c", average_int );
}