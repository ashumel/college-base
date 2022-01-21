#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main() {
    setlocale(LC_ALL, "rus");
    double i = 1;
    const double e = 0.03;
    double s, l;
    do {
    l = 1 / i;
    cout << l << setw(1) << endl;
    s += l; } while (s > e); {
    cout << "Результат: " << s << endl;
    } return 0; }