#include <iostream>
#include <math.h>
using namespace std;

int main() {
    double f, f2, x, a, b, h;
    const double e = 2.72;
    cout << "Введите A:" << endl;
    cin >> a;
    cout << "Введите B:" << endl;
    cin >> b;
    cout << "Кол-во шагов: " << endl;
    cin >> h;
    while (a <= b) {
        f = (pow(e, x) * cos(x) + cos(1));
        f2 = f / tan(x); 
        a += h;
        cout << f << endl; }
    return 0; }