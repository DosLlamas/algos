// UCF Local Contest 2025 (Qualifying) - Who wants to be a Millionaire?
// Solution written by Tyler Marks

#include <bits/stdc++.h>
using namespace std;

int main() {
    // Scan in the input
    int n; cin >> n;
    vector<int> w(n+1);
    for(int i = 0; i < n; i++) 
        cin >> w[i+1];

    vector<double> p(n), q(n);
    for(int i = 0; i < n; i++) 
        cin >> p[i];
    for(int i = 0; i < n; i++) 
        cin >> q[i];

    // Initalize the dp table
    vector dp(n, vector(3, -1.0));

    // Recursive function for computing answer
    // STATE: current question and how many times weve been helped
    function<double(int,int)> calc = [&](int idx, int used) -> double {
        // BASE CASE: if the index hits n, we win with the prize at w[n]
        if(idx == n) return w[idx];

        // Check if this state has been seen
        if(dp[idx][used] != -1.0)
            return dp[idx][used];
        
        // TRANSITIONS:
        // Cash out
        double stop = w[idx];
        // Attempt question on own
        double self = p[idx] * calc(idx+1, used);
        // Attempt to ask expert
        double expert = used < 2 ? q[idx] * calc(idx+1, used+1) : 0;

        // Memoize and return the answer
        return dp[idx][used] = max({stop, self, expert});
    };

    // Output the answer with 10 decimal places
    cout << fixed << setprecision(10);
    cout << calc(0, 0) << '\n';
}