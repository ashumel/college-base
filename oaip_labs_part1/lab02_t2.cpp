#include <iostream>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int mounth, days;
    cout << "Введите число месяца:" << endl;
    cin >> mounth;
    switch (mounth) {
        case 1:
        days = 31;
        break;
        case 2:
        days = 28;
        break;
        case 3:
        days = 31;
        break;
        case 4:
        days = 30;
        break;
        case 5:
        days = 31;
        break;
        case 6:
        days = 30;
        break;
        case 7:
        days = 31;
        break;
        case 8:
        days = 31;
        break;
        case 9:
        days = 30;
        break;
        case 10:
        days = 31;
        break;
        case 11:
        days = 30;
        break;
        case 12:
        days = 31;
        break; }
    cout << "Количество дней в этом месяце: " << days << endl;
    return 0; }