#include <iostream>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int x;
    cout << "Введите число:" << endl;
    cin >> x;
    if (x >= 1) {
        cout << ++x << endl;
    } else {
        cout << ----x << endl;
    } return 0; }