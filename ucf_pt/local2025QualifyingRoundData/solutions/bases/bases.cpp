// Arup Guha
// Alternate Solution to 2025 UCF Locals Qualifying Problem: Cover Your Bases
// 8/2/2025

using namespace std;
#include <bits/stdc++.h>

int convert(string s, int b);

int main() {

    // Read in everything.
    string x, y, s;
    cin >> x >> y >> s;
    int target = convert(s, 10);
    bool done = false;

    // Try all options.
    for (int b1=2; b1<=10; b1++) {
        for (int b2=2; b2<=10; b2++) {

            // Convert in these bases.
            int v1 = convert(x, b1);
            int v2 = convert(y, b2);

            // Not viable.
            if (v1 == -1 || v2 == -1) continue;

            // Found it.
            if (v1+v2 == target){
                cout << b1 << " " << b2 << endl;
                done = true;
                break;
            }
        }

        // Avoid double printing.
        if (done) break;
    }

    return 0;
}

// Returns s in base b, returns -1 if that base is impossible.
int convert(string s, int b) {
    int res = 0;
    for (int i=0; i<s.size(); i++) {
        int digit = s[i]-'0';
        if (digit >= b) return -1;
        res = b*res + digit;
    }
    return res;
}
