#include <iostream>
#include <iomanip>
#include <set>
using namespace std;
int main() {
    set <int> s, s1, s2;
    int n, m, x, count;
    cout << "Введите количество элементов первого списка: " << endl;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Введите ваше число: " << endl;
        cin >> x;
        s1.insert(x);
    } cout << endl << "Введите количество элементов второго списка: " << endl;
    cin >> m;
    for (int i = 0; i < m; i++) {
        cout << "Введите ваше число: " << endl;
        cin >> x;
        s2.insert(x);
    } for (auto now = s1.begin(); now != s1.end(); now++) {
		for (auto now1 = s2.begin(); now1 != s2.end(); now1++) {
			if (*now == *now1) {
				s.insert(*now);
			}
		}
	}
	cout << " " << endl;
	cout << "Общее количество элементов из первого и вторго списка: " << s.size() << endl;
	system("pause");
	return 0;
}