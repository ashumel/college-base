#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int i, k, n; 
    cout << "Введите число: " << endl;
    cin >> k; 
    cout << "Сколько раз его продублировать: " << endl;
    cin >> n;
    cout << "Выходные данные: " << endl;
    for (i = 0; i < n; i++) { 
    cout << k << setw(1) << endl; }
return 0; }