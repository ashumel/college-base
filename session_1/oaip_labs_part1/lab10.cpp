#include <iostream>
using namespace std;

struct train {
    int number;
    string name;
    int time1;
    int time2;
}; 
int main() {
    const int n = 3;
    struct train table[n];
    cout << "Введите информацию о поездах" << endl;
    for(int i = 0; i < n; i++) {
        cout << "Введите номер поезда: ";
        cin >> table[i].number;
        cout << "Введите конечную станцию: ";
        cin >> table[i].name;
        cout << "Введите время отправления в часах: ";
        cin >> table[i].time1;
        cout << "Введите время прибытия на конечную станцию в часах: ";
        cin >> table[i].time2;
    } for(int i = 0; i < n; i++) {
        cout << table[i].number << " " << table[i].name << " " << table[i].time1 << " " << table[i].time2 << endl;
    }
    string station;
    cout << "Введите станцию: ";
    cin >> station;
    for (int i = 0; i < n; i++){
        if (table[i].name == station){
            int time3 = table[i].time2 - table[i].time1;
            cout << table[i].number << " " << table[i].name << " " << table[i].time1 << " " << table[i].time2 << " " << time3 << endl;
        } } return 0; }