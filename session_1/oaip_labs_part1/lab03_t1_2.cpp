#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int i, a, b, n;
    n = 0; 
    cout << "Введите от какого числа начать: " << endl;
    cin >> a; 
    cout << "На каком числе закончить: " << endl;
    cin >> b;
    cout << "Выходные данные: " << endl;
    for (i = a; i < b + 1; i++) {
        cout << i << setw(1) << endl;
        n++; 
    } cout << "Всего чисел выведено = " << n << endl; 
return 0; }