
// Header with input output
#include <iostream>

// To avoid using std:: everywhere
using namespace std;

// The main function (entry point of the program)
int main() {
   // Read in the apples per bag, bags, and cost per dozen
   int apb, bs, cpd;
   cin >> apb >> bs >> cpd;

   // Compute the number of dozens
   int ds = (apb * bs + 11) / 12;

   // Print the total cost based on the number of dozens and cost per dozen
   cout << ds * cpd << endl;

   // Exit
   return 0;
}
