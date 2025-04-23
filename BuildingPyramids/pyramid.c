#include <stdio.h>

int main() {
    int blocks;
    scanf("%d", &blocks);

    int height = 0;
    int used = 0;
    int layer_size = 1;

    while (1) {
        int need = layer_size * layer_size;
        if (used + need > blocks) break;
        used += need;
        height++;
        layer_size += 2;
    }

    printf("%d\n", height);
    return 0;
}
