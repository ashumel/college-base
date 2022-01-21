#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

int main(){
    double a, b, c, s, p;
    cout << "Введите периметр равностороннего треугольника: " << endl;
    cin >> p;
    c= p / 3;
    a= c*c*sqrt(3);
    s= a / 4;
    cout << "Площадь треугольника равна: " << s << endl;
return 0; }