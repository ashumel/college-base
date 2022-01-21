#include <iostream>
using namespace std;
int recursia(int num) {
if (num / 10 != 0)
return num % 10 + recursia(num / 10);
else return num % 10;
}

int main() {
setlocale(LC_ALL , "rus");
cout << "Введите число: " << endl;
int number;
cin >> number;
cout << "Сумма всех цифр: " << recursia(number) << endl;
}