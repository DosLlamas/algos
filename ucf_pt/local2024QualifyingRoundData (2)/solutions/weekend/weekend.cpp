
#include <bits/stdc++.h>

using namespace std;

using ld = long double;
using ll = long long;

using vd = vector<ld>;
using vvd = vector<vd>;
using vvvd = vector<vvd>;

int main() {
   ll lo, hi;
   cin >> lo >> hi;

   ll c[3], a[3];
   for (int i = 0; i < 3; i++) cin >> c[i];
   for (int i = 0; i < 3; i++) cin >> a[i];
  
   vvvd memo(a[0]+1, vvd(a[1]+1, vd(a[2]+1)));
   memo[0][0][0] = 1;
   ld ans = 0;
   for (int i = 0; i <= a[0]; i++)
      for (int j = 0; j <= a[1]; j++)
         for (int k = 0; k <= a[2]; k++) {
            ll cc = i*c[0] + j*c[1] + k*c[2];
            if (cc > hi) continue;
            if (cc >= lo) {
               ans += memo[i][j][k];
               continue;
            }
            ld left = (a[0]+a[1]+a[2]) - (i+j+k);
            if (i < a[0])
               memo[i+1][j][k] += memo[i][j][k] * (a[0]-i) / left;
            if (j < a[1])
               memo[i][j+1][k] += memo[i][j][k] * (a[1]-j) / left;
            if (k < a[2])
               memo[i][j][k+1] += memo[i][j][k] * (a[2]-k) / left;
         }

   cout << setprecision(12) << fixed << ans << endl;

   return 0;
}
