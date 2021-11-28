#include <iostream>
#include <iomanip>
#include <set>
using namespace std;
int main() {
    set <int> s;
    int n, count;
    cout << "Введите количество элементов списка: " << endl;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cout << "Введите число: " << endl;
        cin >> x;
        s.insert(x);
    } for(auto now = s.begin(); now != s.end(); now++) {
        cout << *now << setw(2);
        count++;
    } cout << endl <<"Количество разных чисел: " << count;
    return 0; }