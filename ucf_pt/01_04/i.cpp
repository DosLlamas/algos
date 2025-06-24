#include <iostream>
#include <cmath>
using namespace std;

/* 
FPT
-Bob can see the upperhalf of n digits of his score and Alice's score. Alice can see the lower-half of her score and the upper-half of Bob's score.
-Half is meant to include the horizontal segments in the digits' centers. 
-Output the number of score pairs that can be displayed on the two n digit displays and are fully known to both Bob and Alice.
-Fully known means that both players know both scores.

 */

int main() {
    int n;
    cin >> n;
    long long int result = pow(8, n);
    cout << result;
    return 0;
}