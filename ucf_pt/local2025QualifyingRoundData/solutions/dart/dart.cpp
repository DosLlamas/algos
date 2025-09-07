// Arup Guha
// Alternate Solution to 2025 UCF Locals Qualifying Problem: Simplified Dart Game
// 8/2/2025

using namespace std;
#include <bits/stdc++.h>

int main() {

    // Read in everything.
    int n, r, c;
    cin >> n >> r >> c;

    // Here is the calculation we want. Max distance horizontal or vertical.
    int dist = max( abs((n+1)/2-r),abs((n+1)/2-c) );

    // Then we multiply that by 10 and subtract from the bullseye score.
    cout << 100 - 10*dist << endl;

    return 0;
}
