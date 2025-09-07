// UCF Local Contest 2025 (Qualifying) - World Population
// Solution written by Tyler Marks

#include <bits/stdc++.h>
using namespace std;

using ll = long long;

// Binary Index Tree code
struct BIT {
    vector<ll> bit;
    BIT(int n): bit(n, 0) {}
    // add d to arr[i]
    void update(int i, ll d) {
        for(; i < size(bit); i |= i+1)
            bit[i] += d;
    }
    // query sum of all arr[j] s.t. j < i
    ll query(int i) {
        ll res = 0;
        for(; i > 0; i &= i-1)
            res += bit[i-1];
        return res;
    }
};

int main() {
    // Scan in number of countries
    int n; cin >> n;

    // Initialize BIT
    BIT bit(n);

    // Scan in initial populations
    for(int i = 0; i < n; i++) {
        int v; cin >> v;
        bit.update(i, v);
    }

    // Scan in number of queries
    int q; cin >> q;

    // Process each query
    while(q--) {
        char c; cin >> c;
        // Update a countries population
        if(c == 'U') {
            int i, d; cin >> i >> d;
            bit.update(i-1, d);
        }
        // Find the sum of a range of populations
        else {
            int l, r; cin >> l >> r;
            cout << bit.query(r) - bit.query(l-1) << '\n';
        }
    }
}