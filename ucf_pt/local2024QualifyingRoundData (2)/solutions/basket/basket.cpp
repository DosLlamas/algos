
// Header files for utility
#include <bits/stdc++.h>

// To ensure we can use all the standard library stuff without explicitly
// stating so every time
using namespace std;

// Function to read shots made from the user and return the resulting score
int getScore() {
   int p1, p2, p3;
   cin >> p1 >> p2 >> p3;
   return p1 * 1 + p2 * 2 + p3 * 3;
}

// The main function (starting point of the program)
int main() {
   // Get the scores from the user
   int score1 = getScore();
   int score2 = getScore();

   // Check for the winner
   if (score1 < score2) {
      cout << "2\n";
   } else if (score1 > score2) {
      cout << "1\n";
   } else {
      cout << "0\n";
   }

   // Exit the program
   return 0;
}
