#include <iostream>
using namespace std;
struct class8 { // Создаем структуру
    bool informatic;
    bool biologic;
    bool english;
    bool math; };
int main() {
    struct class8 andrey; 
    cin >> andrey.informatic >> andrey.biologic >> andrey.english >> andrey.math; // Заполняем структуры
    cout << endl;
    struct class8 egor;
    cin >> egor.informatic >> egor.biologic >> egor.english >> egor.math;
    cout << endl;
    struct class8 ksuha;
    cin >> ksuha.informatic >> ksuha.biologic >> ksuha.english >> ksuha.math;
    cout << endl;
    struct class8 igor;
    cin >> igor.informatic >> igor.biologic >> igor.english >> igor.math;
    cout << endl;
    if(andrey.english) cout << "Андрей занимался английским языком";
    else if(egor.english) cout << "Егор занимался английским языком";
    else if(ksuha.english) cout << "Ксюша занимался английским языком";
    else if(igor.english) cout << "Игорь занимался английским языком"; // Выводим ответ 
    }
/* class8 andrey = {false, true, false, true};
    class8 egor = {true, false, false, false};
    class8 ksuha = {false, false, false, true};
    class8 igor = {false, false, true, false};
    if(igor.english == true) {
        cout << "Игорь занимался английским языком"; */