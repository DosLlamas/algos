#include <iostream>
#include <cmath>
using namespace std;

/* 
FPT
-given the coordinates of the points of a triangle and an expected radius of the inner circle
-formula to calculate the radius of the inner ciricle: r = 2A/(a+b+c) where A is the area of the triangle and a,b,c are the lengths of the sides of the triangle
-need to find the area of the triangle and the lengths of the sides
-need to find the area of the triangle using the coordinates of the points
-need to find the lengths of the sides using the coordinates of the points
-know the coordinateds so I can calucate the lengths of each side
-area of a triangle is 1/2 * base * height. The base is the length of the side of the triangle and the height is the distance from the base to the opposite vertex
1. 
-Read input of each coordinate
-Calculate the length of each side
-Calculate the area of the triangle
-Calculate the radius of the inner circle
2.
Return the radius of the inner circle - the expected radius of the inner circle


 */

int main(){
    double x1, y1, x2, y2, x3, y3, r;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> r;
    // Calculate the lengths of the sides
    double a = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    double b = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
    double c = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2));

    // Calculate the area of the triangle using the determinant method
    double area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2));

    // Calculate the radius of the inner circle
    double radius = 2 * area / (a + b + c);

    // Output the difference between the expected radius and the calculated radius as a percentage value
    cout << 100 * (radius - r) / r << endl;
    return 0;
}
