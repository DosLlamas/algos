// UCF Local Contest 2025 (Qualifying) - Country Roads
// Solution written by Tyler Marks

#include <bits/stdc++.h>
using namespace std;

// Disjoint Set Data Structure
struct DSU {
   vector<int> e;
   DSU(int n): e(n, -1) {}
   int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
   int join(int x, int y) {
      x = find(x), y = find(y);
      if(x == y) return false;
      if(e[x] > e[y]) swap(x, y);
      e[x] += e[y]; e[y] = x;
      return true;
   }
};

int main() {
    // Scan in number of cities, inital edges
    // add candidate edges
    int n, m, r; cin >> n >> m >> r;
    
    // Initialize the DSU
    DSU dsu(n);

    // Scan in the inital edges and join the
    // corresponding nodes together
    for(int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        u--, v--;
        dsu.join(u, v);
    }
    
    // Scan in the candidate edges
    vector<array<int, 3>> new_edges(r);
    for(auto &[w, u, v]: new_edges) {
        cin >> u >> v >> w;
        u--, v--;
    }

    // Sort the edges by weight, allowing us
    // to greedily build the remaining edges
    // (essentially using kruskal's algorithm)
    sort(begin(new_edges), end(new_edges));

    // Go through the edges and if joining the
    // incident nodes is successful, add the
    // edge weight to the answer
    int res = 0;
    for(auto [w, u, v]: new_edges)
        if(dsu.join(u, v))
            res += w;

    // Output the answer
    cout << res << '\n';
}