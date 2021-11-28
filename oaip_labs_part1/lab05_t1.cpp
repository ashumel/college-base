#include <iostream>
using namespace std;

int main() {
    double i = 0;
    cout << "Введите число: " << endl;
    cin >> i;
    while(i <= 100) {
        cout << "Введите число больше 100: " << endl;
        cin >> i;
    }
    cout << i;
return 0; }