#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int i, n;
    double s, l;
    n = 15;
    for (i = 1; i <= n; i++) {
        l = 1 / (pow((2 * i + 1), 2));
        cout << l << setw(1) << endl;
        s += l; 
    } 
    cout << "Результат: " << s << endl;
return 0; }