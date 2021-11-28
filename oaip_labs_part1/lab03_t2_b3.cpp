#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int i, n;
    double x, s, l;
    n = 100;
    x = 5.7;
    for (i = 1; i <= n; i++) {
        l = (pow((-1), i)) * (pow(x, 2) / i);
        cout << l << setw(1) << endl;
        s += l; 
    } cout << "Результат: " << s << endl;
return 0; }