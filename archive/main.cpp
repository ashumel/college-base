#include <iostream>
#include <stdio.h>

using namespace std;

struct person
{
    char name[20];
    float ball;
    int nummer;
};
int main(){   
    const int n = 2;
    float result2, result;
    struct person VGKE[n];
    for (int i = 0; i < n; i++) {
        cout << "Введите Имя учащегося " << endl;
        cin >> VGKE[i].name;
        cout << "Введите Балл учащегося " << endl;
        cin >> VGKE[i].ball;
        cout << "Введите Номер учащегося " << endl;
        cin >> VGKE[i].nummer;
        cout << " " << endl;
    }
    for (int i = 0; i < n; i++) {
        cout << VGKE[i].nummer << " " << VGKE[i].name << " " << VGKE[i].ball << endl;
    }
    for (int i = 0; i < n; i++) {
        if (VGKE[i].ball <= 4) cout << VGKE[i].name << " " << VGKE[i].nummer;
    } 
    for (int i = 0; i < n; i++) {
        result += VGKE[i].ball;
    } result2 = result / 2;
    cout << "Средний балл учеников: " << result2;
    return 0;
}