// Arup Guha
// 8/2/2025
// Alternate Solution to 2025 UCF Locals Qualifying Problem: Social Security Benefits

using namespace std;
#include <bits/stdc++.h>

int main() {

    // Read in everything.
    int a1, m1, a2, m2, a3;
    cin >> a1 >> m1 >> a2 >> m2 >> a3;

    // This is when we take the first option...
    if ((a3-a1)*m1 >= (a3-a2)*m2)
        cout << "1" << endl;
    else
        cout << "2" << endl;

    return 0;
}
