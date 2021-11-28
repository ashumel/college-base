#include <iostream>
#include <math.h>
using namespace std;

int main() {
    double f, x, a, b, h;
    cout << "Введите A:" << endl;
    cin >> a;
    cout << "Введите B:" << endl;
    cin >> b;
    cout << "Кол-во шагов: " << endl;
    cin >> h;
    while (a <= b) {
        f = pow(a, 2) - 2 * cos(a); 
        a += h;
        cout << f << endl; }
    return 0; }