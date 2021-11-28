#include <iostream>
using namespace std;

void d(int a, int b){
    if (a <= b) {
    if (a == b) {
        cout << a << endl;
        return;
    } cout << a << endl;
    a = a + 1;
    d(a,b);
    } if (a >= b) {
    if (a == b) {
        cout << a << endl;
        return;
    } cout << a << endl;
    a = a - 1;
    d(a, b);
    } }
int main() {
    setlocale(LC_ALL, "rus");
    int a;
    int b;
    cout << "Введите число а : " ;
    cin >> a;
    cout << "\n Введите число б : " ;
    cin >> b;
    cout << "\n Итог : ";
    d(a, b);
    //cout << res << endl;
    return 0;
}