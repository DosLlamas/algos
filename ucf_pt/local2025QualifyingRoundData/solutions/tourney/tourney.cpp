// Arup Guha
// 8/2/2025
// Alternate Solution to 2025 UCF Locals Qualifying Problem: Single Elimination Tournament

using namespace std;
#include <bits/stdc++.h>

int main() {

    // Read in input.
    int n;
    cin >> n;

    // Get highest one bit...
    int highbit = 0;
    while ( (1<<highbit) <= n ) highbit++;
    highbit--;

    // We find the highest power of 2 <= n.
    // Then subtract this from n to give the of winning teams
    // in the prelims...multiply by 2 to get # of teams in prelims.
    cout << ((n-(1<<highbit))<<1) << endl;

    return 0;
}
