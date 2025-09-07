// UCF Local Contest 2025 (Qualifying) - Judge Meetings
// Solution written by Tyler Marks

#include<bits/stdc++.h>
using namespace std;

int main() {
    // Scan in number of coaches and days
    int n, m; cin >> n >> m;

    // store a frequency array storing how many
    // coaches are out on each day
    vector<int> frq(m+1);

    // Scan in each coaches vacations
    for(int i = 0; i < n; i++) {
        int v; cin >> v;
        for(int j = 0; j < v; j++) {
            int s, e; cin >> s >> e;

            // Update frequency for each day in range
            for(int k = s; k <= e; k++)
                frq[k]++;
        }
    }

    // Count how many days have enough coaches
    int res = 0;
    for(int i = 1; i <= m; i++)
        if(n - frq[i] >= 3)
            res++;

    // Output the answer
    cout << res << '\n';
}