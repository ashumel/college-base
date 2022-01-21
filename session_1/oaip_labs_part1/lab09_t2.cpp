#include <iostream>
#include <iomanip>
#include <set>
using namespace std;
int main() {
    set <int> s;
    int n;
    cout << "Введите количество элементов списка: " << endl;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cout << "Введите число: " << endl;
        cin >> x;
            if (s.find(x) != s.end())
            cout << "yes" << endl;
            else {
            s.insert(x);
            cout << "no" << endl; }
    } return 0; }