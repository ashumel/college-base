#include <iostream>
#include <math.h>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    double x, y, z;
    cout <<"Введите X: ";
    cin >> x;
    cout <<"Введите Y: ";
    cin >> y;
    cout <<"Введите Z: ";
    cin >> z;
    double n1, n2, a;
    n1 = sin(x-y);
    n2 = fabs(x) + pow((cos(z)), 2) + 1;
    a = n1 / n2;
    cout << a << endl;
return 0; }