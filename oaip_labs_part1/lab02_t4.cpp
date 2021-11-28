#include <iostream>

using namespace std;

int main() {
    int a, b;
    cout << "Введите A: ";
    cin >> a;
    cout << "Введите B: ";
    cin >> b;
    cout << ((a + b < 20) ? "Мало" : "Много");
    return 0; 
}