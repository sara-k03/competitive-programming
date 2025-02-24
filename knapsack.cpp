#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii; 
typedef vector<int> vi;  

int main() {
    int n, k; // n --> number of items, k --> max weight capacity
    cin >> n >> k; 

    vi w(n);
    vi v(n);
    
    for (int &x : w) cin >> x; 
    for (int &x : v) cin >> x; 

    vi T(k + 1, 0);
    
    for (int i = 0; i < n; i++) {
        for (int j = k; j >= w[i]; j--) {
            T[j] = max(T[j], T[j - w[i]] + v[i]);
        }
    }

    int ans = T[ 0 ];
    for ( int j = 1; j <= k; j++ ) {
        ans = max( ans, T[ j ] );
    }

    printf( "%d\n", ans );

    return 0;
}

// g++ -o knapsack knapsack.cpp -std=c++17 -O2 
// ./knapsack < knapsack.txt 