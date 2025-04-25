#include <stdio.h>
#include <math.h>

double get_distance(double t,
                    int kx1, int ky1, int kx2, int ky2,
                    int ox1, int oy1, int ox2, int oy2) { // t -> how far into the race, 0 to 1
    double kx = kx1 + t * (kx2 - kx1);
    double ky = ky1 + t * (ky2 - ky1);
    double ox = ox1 + t * (ox2 - ox1);
    double oy = oy1 + t * (oy2 - oy1);
    return sqrt((kx - ox) * (kx - ox) + (ky - oy) * (ky - oy));
}

int main() {
    int kx1, ky1, ox1, oy1, kx2, ky2, ox2, oy2;
    scanf("%d %d %d %d %d %d %d %d", &kx1, &ky1, &ox1, &oy1, &kx2, &ky2, &ox2, &oy2);

    double low = 0.0;
    double high = 1.0;
    for (int i = 0; i < 100; i++) { // ternary search - split into 3 one-hundred times to isolate low and high
        double t1 = low + (high - low) / 3;
        double t2 = high - (high - low) / 3;
        double d1 = get_distance(t1, kx1, ky1, kx2, ky2, ox1, oy1, ox2, oy2);
        double d2 = get_distance(t2, kx1, ky1, kx2, ky2, ox1, oy1, ox2, oy2);
        if (d1 < d2)
            low = t1;
        else
            high = t2;
    }

    double max_distance = get_distance((low + high) / 2, kx1, ky1, kx2, ky2, ox1, oy1, ox2, oy2);
    printf("%f\n", max_distance);

    return 0;
}
