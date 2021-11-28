#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main() {
    int a, b, d, i;
    cout << "Введите число A: ";
    cin >> a;
    cout << "Введите число B: ";
    cin >> b;
    for (d = a; d < b+1; d++){
        for(i = 0; i < d; i++){
        cout << setw(3) << d;              
        } cout << endl;
    } return 0; }