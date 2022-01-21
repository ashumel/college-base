#include <iostream>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int a, b, result, user;
    cout << "Изучение таблицы умножения\n" << "Введите число A:" << endl;
    cin >> a;
    cout << "Введите число B:" << endl;
    cin >> b;
    result = a * b;
    cout << "Введите результат умножения:" << endl;
    cin >> user;
    if(user != result) {
        cout << "Ответ неверный\n Правильный ответ: " << result << endl;
    } else {
        cout << "Ответ правильный! " << result << endl;
    }
return 0; }