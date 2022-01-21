#include <iostream>
using namespace std;

int main() {
    int m, n; // Вводим две переменые с минутами и секундами
    const int mb = 6; // Задаем свободное дисковое пространство
    const double kb = 16; // Для записи одной секунды звука 
    double kb_user; // Количество свободного пространства в килобайтах
    double result = 0; // Конечный вес файла
    double m_to_n = 960; // 60 сек на 16
    cout << "Введите количество секунд: ";
    cin >> n;
    cout << endl << "Введите количество минут: ";
    cin >> m;
    for(int i; i < mb; i++) { // Конвертируем MB в KB
        kb_user += 1024;
    } for(int i; i < n; i++) {
        result += kb; // Прибавляем к конечному размеру файла секунды
    } for(int i; i < m; i++) {
        result += m_to_n; // Прибавляем к конечному размеру файла минуты
    } cout << "Вес файла в килобайтах: "<< result << endl << kb_user << endl;
    if(result <= kb_user) {
        cout << "Дискового пространства хватит.";
    } else cout << "Дискового простанства не хватит!";
}