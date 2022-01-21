#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a;
    if ( a >= 0 ) {
        b = a + 1;
    } else b = a - 2;
    cout << b;
}