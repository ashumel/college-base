#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>

int rrand(int range_min, int range_max) {
    return rand() % (range_max - range_min + 1) + range_min;
}
using namespace std;
int main() {
    int range_min = -10, range_max = 10, size;
    cout << "Введите количество сгенерированных чисел: ";
    cin >> size;
    int * a = new int[size];
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        a[i] = rrand(range_min, range_max);
        cout << a[i] << setw(4);
    } cout << endl;
    system("pause");
    return 0;
}